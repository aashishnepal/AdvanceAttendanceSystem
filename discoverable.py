import bluetooth
import sqlite3


conn = sqlite3.connect('db.sqlite3')
print("Performing inquiry...")

dis_mac = bluetooth.discover_devices(duration=4, lookup_names=True,
                                            flush_cache=True, lookup_class=False)
print("the discoverable device at this time ", dis_mac)


db_mac = conn.execute("SELECT mac_address from info_student")

for item_db_mac in db_mac:
    print('\n')
    for item in dis_mac:
        if item[0] == item_db_mac[0]:
            conn.execute("UPDATE info_student SET attendence_stat = 1 where mac_address='{}'".format(item_db_mac[0]))
            conn.commit()
            print(item_db_mac[0]," is Present")
            break;

conn.close()
