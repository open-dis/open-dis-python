import tkinter as tk
from tkinter import ttk
from datetime import datetime
import threading
import sqlite3

lock = threading.Lock()

connection = sqlite3.connect('dis_messages_database.db')

class App(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title('DIS Logger')

      table = ttk.Treeview(self, columns=("num", "time", "type", "src", "dst", "ent_id", "ent_marking"), show = 'headings')
      self.table = table

      # Set heading text
      table.heading('num', text='No.')
      table.heading('time', text='Time')
      table.heading('type', text='Message Type')
      table.heading('src', text='Source')
      table.heading('dst', text='Destination')
      table.heading('ent_id', text='Entity ID')
      table.heading('ent_marking', text='Entity Marking')

      # Set column widths
      table.column('num', width=50)
      table.column('ent_id', width=25)

      table.pack()
      table.bind("<Button-1>", self.on_table_click)

      # Set message display
      message_display = tk.Text(self, height=10, width=60)
      self.message_display = message_display
      message_display.pack(pady=10)
      message_display.insert(tk.END, "Click on a table entry to view more")

      # Setup database
      cursor = connection.cursor()
      cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
      tables = cursor.fetchall()

      for table_name in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]};")
      
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS messages (
              number INT PRIMARY KEY,
              time VARCHAR(255),
              type VARCHAR(255),
              source_address VARCHAR(255),
              source_port VARCHAR(255),
              destination_address VARCHAR(255),
              destination_port VARCHAR(255),
              entity_id INT,
              entity_marking VARCHAR(255),
              latitude FLOAT,
              longitude FLOAT,
              altitude FLOAT    
          )
      ''')
      
      connection.commit()
      cursor.close()


   def on_table_click(self, event):
      item_id = self.table.identify_row(event.y)
      if item_id:
          item_values = self.table.item(item_id, 'values')
          item_number = item_values[0]
          self.message_display.insert(tk.END, item_number)
          
          # Get entry based on number in table
          connection = sqlite3.connect('dis_messages_database.db')
          cursor = connection.cursor()
          cursor.execute("SELECT * FROM messages WHERE number=?", (item_number,))
          entry = cursor.fetchall()[0]
          cursor.close()

          # Form message to be displayed
          message = ("Received {}".format(entry[2]) + " at {}\n".format(entry[1])
            + " Sending Addr.  : {}\n".format(entry[3])
            + " Sending   Port   : {}\n".format(entry[4])
            + " Destination Addr.: {}\n".format(entry[5])
            + " Destination Port : {}\n".format(entry[6])
            + " Entity Id      : {}\n".format(entry[7])
            + " Entity Marking : {}\n".format(entry[8])
            + " Latitude       : {:.5f} degrees\n".format(entry[9])
            + " Longitude      : {:.5f} degrees\n".format(entry[10])
            + " Altitude       : {:.0f} meters\n".format(entry[11])
          )

          # Show message in message display
          self.message_display.delete(1.0, tk.END)
          self.message_display.insert(tk.END, message)


   def add_entry(self, entry):
      lock.acquire()

      # Get message info from entry
      num = len(self.table.get_children())
      time = datetime.now()
      type = entry.type
      src_addr = entry.src_addr
      dst_addr = entry.dst_addr
      ent_id = entry.entityID
      ent_marking = entry.marking
      latitude = entry.latitude
      longitude = entry.longitude
      altitude = entry.altitude

      # Add message to table
      data = (num, time, type, src_addr, dst_addr, ent_id, ent_marking)
      self.table.insert(parent='', index=0, values = data)

      # Add message to database
      connection = sqlite3.connect('dis_messages_database.db')
      cursor = connection.cursor()
      db_entry = (num, time, type, src_addr, dst_addr, ent_id, ent_marking, latitude, longitude, altitude)
      cursor.execute('INSERT INTO messages (number, time, type, source_address, destination_address, entity_id, entity_marking, latitude, longitude, altitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', db_entry)
      connection.commit()
      cursor.close()

      lock.release()