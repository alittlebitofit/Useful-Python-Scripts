#! /usr/bin/python

'''
Created on Apr 19, 2012
@author: dan
'''

import pyperclip

 
if __name__ == '__main__':
    import libtorrent as lt
    import time

    import sys
 
    TorrentFilePath = "/home/username/Downloads/"
    TorrentFilePath2 = "/home/username/Downloads/" + "T.torrent"
    ses = lt.session()
    #ses.listen_on(6881, 6891)
    params = {
        'save_path': TorrentFilePath,
        'duplicate_is_error': True}
    link = pyperclip.paste()
#    link = "magnet:?xt=urn:btih:91AF2B3F172B251E5106146D3DDDCB16C0C631D2&dn=%5B+FreeCourseWeb+%5D+The+Complete+2019+Web+Development+Bootcamp+%28Updated+2-2019%29&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fthetracker.org%3A80%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta-net.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Fdenis.stalker.upeer.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.filemail.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.iamhansen.xyz%3A2000%2Fannounce&tr=udp%3A%2F%2Fretracker.netbynet.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.nyaa.uk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftorrentclub.tech%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.supertracker.net%3A1337%2Fannounce&tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"
    handle = lt.add_magnet_uri(ses, link, params)
#    ses.start_dht()
    print 'saving torrent file here : ' + TorrentFilePath2 + " ..."
    while (not handle.has_metadata()):
        time.sleep(.1)
 
    torinfo = handle.get_torrent_info()
 
    fs = lt.file_storage()
    for file in torinfo.files():
        fs.add_file(file)
    torfile = lt.create_torrent(fs)
    torfile.set_comment(torinfo.comment())
    torfile.set_creator(torinfo.creator())
 
    f = open(TorrentFilePath2 + "torrentfile.torrent", "wb")
    f.write(lt.bencode(torfile.generate()))
    f.close()
    print 'saved and closing...'
 
#Uncomment to Download the Torrent:
#    print 'starting torrent download...'
 
#    while (handle.status().state != lt.torrent_status.seeding):
#        s = handle.status()
#        time.sleep(55)
#        print 'downloading...'
