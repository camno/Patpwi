from ib_insync import * 
from asyncio import * 


async def connect_ib_client(paper_trading = True):
    # IB connection 
    HOST = "127.0.0.1"
    if paper_trading == True:
        PORT = 7497
    else:
        PORT = 7496 
    # ID number can be set in the configuration of IB client
    CLIENT_ID = 1

    ib_client = IB() # Creates an instance of the IB client class

    await ib_client.connect(HOST, PORT, CLIENT_ID) # Connects to TWS
    accounts = ib_client.accountSummary()

    print(f"Account currently signed in to TWS is: {accounts[0]}")
    return ib_client

def disconnect_ib_client(ib_client):
    ib_client.disconnect()
    print("IB client is closed.")


async def request_realtime_bars(ib_client, contract):
    # barSize must be 5
    # If True then only show data from within Regular Trading Hours(RTH), 
    # if False then show all data.
    bars = await ib_client.reqRealTimeBars(
        contract, 
        5, # real time bar size in seconds
        'TRADES', 
        useRTH = False)
    
    # bars.updateEvent += onBarUpdate

    return bars




def onBarUpdate(bars, hasNewBar):
    print(bars[-1])