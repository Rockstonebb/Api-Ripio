import time
from src.ripio.RipioRequestApi import RipioRequestApi



def main():
    while True:
        ripio = RipioRequestApi()
        print(ripio.getDataFromApi(endpoint="rate/USDC_ARS"))
        print()
        time.sleep(10)

if __name__ == '__main__':
    print("Ripio Api App")
    main()
    
    