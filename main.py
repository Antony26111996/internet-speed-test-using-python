import speedtest

st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice: '''))

if option == 1:
    download_speed_bps = st.download()
    download_speed_mbps = download_speed_bps / 1_000_000
    print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
elif option == 2:
    upload_speed_bps = st.upload()
    upload_speed_mbps = upload_speed_bps / 1_000_000
    print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(f"Ping: {st.results.ping} ms")
else:
    print("Please enter the correct choice!")
