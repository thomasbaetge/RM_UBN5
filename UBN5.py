import asyncio
from bleak import BleakScanner, BleakClient

uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
       # print(d.name)
              
        if d.address == "CD:3E:48:53:21:4D": #Adjust this to the adress of your bike!!
            myDevice = d
        
    async with BleakClient(myDevice.address) as client:
        svcs = await client.get_services()
      #  print("Services:")
      #  for service in svcs:
      #      print(service)
            
        battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
        print(int.from_bytes(battery_level,byteorder='big'))

asyncio.run(main())
