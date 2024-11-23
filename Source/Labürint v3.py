from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

# Pausifunktsioon
def paus():
    global maailm
    time.sleep(0.25)
    maailm.update()
    
# Funktsioon tegelase vasakule pööramiseks, kontrollib esmalt endise suuna, värskendab suuna andme, kustutab
# maailmast tegelase ja joonistab uue suunaga tegelase
def left():
    global maailm
    global pykkar
    global pykkari_suund
    global pykkar_x
    global pykkar_y
    if pykkari_suund == "n":
        pykkari_suund = "w"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_w, anchor=NW)
 
    elif pykkari_suund == "e":
        pykkari_suund = "n"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_n, anchor=NW)
 
    elif pykkari_suund == "s":
        pykkari_suund = "e"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_e, anchor=NW)
 
    elif pykkari_suund == "w":
        pykkari_suund = "s"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_s, anchor=NW)
     
 # Funktsioon tegelase paremale pööramiseks   
def right():
    global maailm
    global pykkar
    global pykkari_suund
    global pykkar_x
    global pykkar_y
    if pykkari_suund == "n":
        pykkari_suund = "e"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_e, anchor=NW)
 
    elif pykkari_suund == "e":
        pykkari_suund = "s"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_s, anchor=NW)
 
    elif pykkari_suund == "s":
        pykkari_suund = "w"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_w, anchor=NW)
 
    elif pykkari_suund == "w":
        pykkari_suund = "n"
        maailm.delete(pykkar)
        pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_n, anchor=NW)

#Funktsioon tegelase edasi astumiseks    
def step():
    global maailm
    global pykkar
    global pykkari_suund
    global pykkar_x
    global pykkar_y
    global ruudu_suurus
    
    #Kontrollib tegelase suunda
    if pykkari_suund == "n":
        # kontrollib kas saab edasi astuda
        if järgmine_vaba("n"):
            maailm.delete(pykkar)
            pykkar_y -= ruudu_suurus
            pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_n, anchor=NW)
        else :
            messagebox.showinfo(message="Sinna ei saa minna!")
            puhasta()
            
    elif pykkari_suund == "e":
        if järgmine_vaba("e"):
            maailm.delete(pykkar)
            pykkar_x += ruudu_suurus
            pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_e, anchor=NW)
        else :
            messagebox.showinfo(message="Sinna ei saa minna!")
            puhasta()

    elif pykkari_suund == "s":
        if järgmine_vaba("s"):
            maailm.delete(pykkar)
            pykkar_y += ruudu_suurus
            pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_s, anchor=NW)
        else :
            messagebox.showinfo(message="Sinna ei saa minna!")
            puhasta()

    elif pykkari_suund == "w":
        if järgmine_vaba("w"):
            maailm.delete(pykkar)
            pykkar_x -= ruudu_suurus
            pykkar=maailm.create_image(pykkar_x, pykkar_y, image=pykkar_w, anchor=NW)
        else :
            messagebox.showinfo(message="Sinna ei saa minna!")
            puhasta()


def järgmine_vaba(suund)   :
    global pykkar_x
    global pykkar_y
    global ruudu_suurus
    global maailm_list
    global viga
    global taseme_nr
    global labürint
    if suund == "n":
        järgmine_x=int(pykkar_x / ruudu_suurus  )
        järgmine_y=int((pykkar_y - ruudu_suurus) / ruudu_suurus )
            
    elif suund == "e":
        järgmine_x=int((pykkar_x + ruudu_suurus) / ruudu_suurus )
        järgmine_y=int(pykkar_y / ruudu_suurus )
    
    elif suund == "s":
        järgmine_x=int(pykkar_x / ruudu_suurus )
        järgmine_y=int((pykkar_y + ruudu_suurus) / ruudu_suurus )
        
    elif suund == "w":
        järgmine_x=int((pykkar_x - ruudu_suurus) / ruudu_suurus )
        järgmine_y=int(pykkar_y / ruudu_suurus )
    
    if maailm_list[järgmine_y][järgmine_x] == " " or maailm_list[järgmine_y][järgmine_x] == "." or maailm_list[järgmine_y][järgmine_x] == ">" :
        return True
    
    elif maailm_list[järgmine_y][järgmine_x] == "F":
        
        messagebox.showinfo(message="Sinu võit, pääsesid labürindist välja!")
        taseme_nr +=1
        tase = "tase" + str(taseme_nr) + ".txt"
        fail = open(tase, encoding = "UTF-8")
        labürint = fail.read()
        fail.close
        create_world(labürint)
        puhasta()
        return True
       
    else:
        
        return False
    
def vasakule ():
    käsud.create_image (käsud_xy(),image = vasakule_ikoon)
    programm.append("left()")

def liigu ():
    
    käsud.create_image (käsud_xy(),image = liigu_ikoon)
    programm.append("step()")

def paremale ():
    
    käsud.create_image (käsud_xy(),image = paremale_ikoon)
    programm.append("right()")

def puhasta ():
    
    programm.clear()
    käsud.delete("all")
    global x
    x=0
    global y
    y=0
    global labürint
    
   # close()
    create_world(labürint)
    
def start ():
    
    global programm
    
    for a in programm:
        if a== "left()":
            left()
            paus()
        if a=="right()":
            right()
            paus()
        if a=="step()":
            step()
            paus()
    puhasta()   
 
# lisafunktsioon käsuikoonide paigutamiseks käsuaknasse
def käsud_xy():
    global x
    global y
    
    if x==3 and y==7:
        messagebox.showinfo(message="Rohkem käske ei mahu!")
        return x_koordinaadid [3], y_koordinaadid [7]    
    
    if y==7:
        x+=1
        y=0
        return x_koordinaadid [x-1], y_koordinaadid [7]
    
    y+=1
    return x_koordinaadid [x], y_koordinaadid [y-1]


fail = open("tase1.txt", encoding = "UTF-8")
labürint = fail.read()
fail.close

taseme_nr = 1
# käsuakna ruudustiku (ikoonide asukohtade) koordinaadid
x_koordinaadid = [30,90,150,210]
y_koordinaadid = [30,90,150,210,270,330,390,450]

#ridade ja veergude loenddurid
x=0
y=0

#käskude järjend
programm = []

pykkari_suund = ""
pykkar_x=0
pykkar_y=0

maailma_laius = 0
maailma_kõrgus = 0
#maailma suuruse määramine
ruudu_suurus = 32

maailm_list = []

raam = Tk()
raam.title("Labürint")
raam.grid()

liigu_ikoon = PhotoImage (data = """
        R0lGODlhNgA2AHAAACH5BAEAAPwALAAAAAA2ADYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/w
        BVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgD
        VmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNV
        ZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/AD
        P/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAA
        GaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5k
        AAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5
        mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZ
        swrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVm
        czVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP
        +AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAAAj/ACfc
        aDChwY2CDXo0IDiw4MGFAxdKZCBR4sOECwUSNIhQYcaBCg+C5DiygY0GDG4wgGGAZQwDNlKmRPkwpEabDUfy2LhzAgOFPh
        XKPGAAgNGjSAEQpThSoASMEgQGXQh0pMKrBmkmBaDCgAoYX7cCoGhDKsYePSZMwJp27Vm1aQ1SRKpCyyJFu7ztKrdrF627W
        lQgPcBAaturbuEmVHswrcKTSGEs0rWLXDld5chpzpy5ryItRw2oNLy29GHTij0ehYHXMrnKnS93dp15EWijohnDLdj2IGmBDIoCYP2NM
        2bLx2Ujl41Z1yLBAAxwTNt4rWPTGA8YhUGrcnPjs5lz/6ZNrhYM3GUXU9+9vkdwo1r2WgZ/PO8iWvTFv759gGPptb755p52AIBRi2aVJU
        gbZooMp4hy4822y20G/PTbdRHBdyBf5Cn4DRhHqYDfayQq2NltVLnl2GIT2GCUCgoul9xrDUb2YH0LZmaeUSnt9t9ARamgiGuwLYefLo
        SIpcKGOIJHi1H9VSdlA0aBsVdy37m2iFjb1YKZNxIuV2N6p6kUZGUyjlcZiFxudySEydFyHgCL1VRQlfPNKNtfbUa2SI4ybjmWem6dB+NlR
        JJ4WY19rtadaxtCet4BvpVGJQBh0GKZia95I2ijkb1ZIom3UUSdSUY9SJteyDEKKl2qFv/JWY0NtaUdDExCyOerYrGmZonnSUfdezDAKRu
        bvPbqJYT7RSdlAABokaZltGgBg7XWQtcnDNfCsMW1M8LGJkFqvfdnhN+Vw1k5yHK5JHj5WUYrQzekOqqs5HznqpK6LIegoiQKWphal
        y7yq3jjfcolDFfGZhmrswpmUEj2clqkvo1y56+/CtbCI1wMGBVpeABnpoi2vaq7XJGyzqtRlfodCNub5Shyl82K4Gzzm1gaWyO5ChVFSHjhE
        qnLX0jvjPOInYGZqLhGgSRQUVo0Oapyu6C8lZWKfqcnaLkhdCag4FE7J5dalD2ezOUFmxBaAqV62Tc947jL2WINyfLV1Br/5d/LAKgaZtk
        7tmlwyV1fNu7bbhWFa5ZNt0zIzWDcfNej5fAMnjcxRGehVCrJPS19fu1ci9LLIs7yvNfFpZ0KkI9+G5eCkxhpgiiy6FboAJyrC93GktNuUjACDF
        tyP1dH2g1B1l52ZYX0iXnPr9ECnYUCMrYQfArundnwkeVqPDlz+ndab8LFl/hyChNPWaLMCZrbdaTFJZzgXxZJS+WEgJHzFoqoHPxI9I0a9
        ccwjFtRSIRjII69JkIRulp9GNWj06gIO5eKlvfuxbem6QhZ06mfYrDDvO20Rm3+Glz15iQd5a2nfuoxiHDqkjr92NB2yBINQRBzmNb9Jy4DCR
        EYmWgxstglqFpni0GKMPSfxLRndw0Qjgnvk5fIEREMs4vOEne4mwCh5oK9aQBR6MItLZjRWnjTotR8mD3s0K83a5mJAQjUKKIMREqlq
        c4bfYQYPSpmICeZoyCJQpimWPAwXPQiD1HTR0vdMSuPVOQF/chDHyKGRadpwE5MghKUyKQBT8meJQnVFieyZ5KMZMwdecNG3ZhSKm4JCAA7""")

start_ikoon = PhotoImage (data = """
        R0lGODlhNwA2AHAAACH5BAEAAPwALAAAAAA3ADYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArz
        AAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAA
        DVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTM
        rzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADP
        VMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGY
        r/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZ
        mbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZpl
        VmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M
        5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM
        8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZ
        v8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+q
        zP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAAAj/ACf0mCCQ4MCCCA8ObNCjwYQGNxpIhPhw
        wg2DGBNmPHix4cCODC0KZCjxBoMGBmAYWKmSwQEbFC+GBPlxZM2CA3PiLCgT5koAQIMKBbqSwcWOO3XqHMm0IdO
        eB4amfHkDhg0DKqQ2MPpwIUeMPZQmHYlSqNUzbdJeSsu2jY0bQg+cROoRp0OROUM6NRnUwA20bTq1uTQn8BzCaw+3q
        Rp0blK9GS8+LQvURlrBggNrXov5ctobWQEYONkVY8ixHxkYAAoDLWHNgg8Xlg27DW0YQAPArKnUq82tUQHcGFw4c2zEsh
        O/Rpz2TOOIOyXnJYsbgGXbyDl71kz79fE2Z1YD/6AoEiFdi+KHMzduu3Zy2p07FXYu+qRY8w/F2yB8vHjtzYX9x55g9B0QEW/RN
        cAadtgVhhxxr71HnCX+cRcGUeV91ZBqAMDgmWAPcpedew/2x4YNQEmE4EJwCSeif+8xB992ioGoWBtZGQDZb5Vp5qONlmDH
        RnFDKidhJ0UyiKJwDi00EgNA3TDgiyICGBgb33Um4WoG2IDXQzes5uGMMGZXpoNnEufjJS02aRdQPGi33I1tmAFYbTau1QYbZ5i
        hlmJzZFbZaRFBCYBnyclRZwy4xdDhDX4impYZoAUAwwEwQMpgZrgdQBJBN0TlYX96hrmCAafGEIAKugF4iQ2OYv9q6aoHgNFg
        YC0yoJOh6gGalg0rABDDX3WamqmSs9oQxhk32HCACgeE0eAlPKTIUENhAhDnjGYEG4OfmbURhgGW+gjDqdL6F8azBrChXRu
        4ndYQUGfMxlwMBsTAA5WgDferpcN19u8KN9jbBlEgGXpGZ4Sd0Sieg4EH4aUq9CAjYWGoBMODuJFmkYKHcheYsyr4S2ZtjsbAV
        nzhraCymp3eEFYDS2K5aVW6MQfeW2BomlajbFAJbwDt+oebjgRJBIAKH9p2YQzXCYZiysLG2YalKl88xxkpQ+gWAAdwBLLXh/XQ
        dWxcwwqsAdIObUC97YF4MKN/tsElUkv2MO0cZsD/UK7Xn6HKg2CgZXqJlm45GrBm1s5clg1armVq1LCZAXBa45Z7WJKMBuDna2
        dkpatBj0ecnMOWAnZj5/UK5jcMMQS9FhuOuujdkhR9FNy07VUVVQw9vwUttGboiTqqzYYKbWveLSbaaQwp/OJaqPuNqmhQw432
        uasFuzxgcq9mYHSVUSg0pbC/Rax2N/Jwww1Q35CuyGYAxUBCEhnqWfNt/UnYkRFri43MJRrohGUkNwiAdW6VHflcjIExml5gCoQ
        UnHCIaSQKUPMEFrkI0gZez/uNV0BGuRoZhn/JgeCtjlMt0XzJLlsBShgUtcH9AXCAeapR/cB2IIPU5SNEOYOZ/2yowhnFRk3OAwBX
        bqIQkhBlZRCaDYU4YzP+cUIzV0RSdcgjlrp8jChmEIyiSLXCTYnsNUn0C+k0UhOagextP1LTdwA4ouroCDJelA4CQbbAElnJRja7VXg
        QxhPU7MQiRgnKdeIoIROGa0lgU5Fd8GcTGIpngUHrj6sqZIPqjMdLXzmkWPQYET5a5wyym16AzADJAjYJj18CCf7y4qyhWMUMPO
        hTn3rQyUs+z4CPWUoX8eMRlARnKKJBpgEMBBlZKqQ0vimmWEhSqKgcMy5+gcgr2VjJZ/rGLl3UZkO0qc0DuWmU3cTJisail3M65
        AYSiF5edIKU8zTlLkoJibya0gwUXX0qQ5EJqFj2ERAAOw==""")

vasakule_ikoon = PhotoImage (data = """
        R0lGODlhMwA0APcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQB
        VzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/w
        D/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVm
        TNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/A
        DP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVz
        GZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Z
        mb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmA
        mZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8w
        AZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMy
        qM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
        M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//V
        Zv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAzADQAAAj/ACdM6CGQ4MCCCAc2m
        NDgRoOHDCA+XNjAoMWEF3tUnHBDIcGOGkM2YHDDgEkAKgAAgAHAAAwGMSJ2BLmR5keMBwnqFOjwpMqfQIEaOE
        CS4c6jBz0qXOrwBoOgKmBoUbSIqqIwWmCk/GmggY2FGpdmFJuToYGfKqbu0lVuF7lybN+Wo7UIzNaWDcGW7Vj2ZsOz
        KmGEYVvu7du4cMm5LVzL7s+iNHNu3KhzpEoVYGgVhssZMeLDhXc5bulQ8tiOfwMvCq3YMOvFbD0XXsQSL8ikShUChlGL
        XOvNrReDBv15lxaVBhgYXV5ZI2AtoTfHrqVos+bh0jkrPg4gBuXczlVC/4/rFnba2Kw7a0/P3QBqixUtA9AiXHg5RSyhD7dPXLpxl
        RHptNMNB6BES3mGuVVLbTD8JptmcX3zm2JbzVTQQ4At4hpitNQGwBbpkdNbdsENpwhyYPF1g3jokdchUFrIVmKI2YmmU
        kMXAjZigiJ6KJ56E9Y341uKpBSgRiXNh+BiLwYVI3AkIgglhOWAoVJp8lXn4IJBibeLN0vymB16hi0CIE8FqkDmXD4GBcObU9Xiz
        XqtffMZZy92NYENZ4EB3C5NdikoADYo0puU5E1YDnc3OKSSlgq2OWiXMCxynZCvkWMmABCpVEtcXE4qKosk0jnXWQz0kC
        Z5J47qqgrVyf+4ZEoHNHAWDNr95+qovAU3p2vbtaQqSmTququoO6oXF0tdnaXfa9wNqpWrMKzp4Bak3WqtsU7WAmgYdwm
        6RX+/HdfsShLSye1PzwY7qJrA7cjlAY6qCVuu0f7U4HpFDprZerGl1NVTKiQL7Lrjpddqlyrca1gtZx3A0aPK4gvUvrItHJSW6vUbka
        0A+Cmmg9GOS6MukoasrpUAzFQgDAfWqaiuuCa62KZu7qiguQs55SmPDsN13LMPhnvZjLTcSNOPxYmpyxZPyliOpAZctxnLE
        XEkH5VSH6azg1WmJPZKhyqWNAD0HtQQqRtKiKi6CR6oy1qfroc1XwSBDICGUgb/uSHAUALLWb9p9zDgrVavabNrYAINdo8q
        fSUQR1o34OXBj1esKHa6cPeQ4Qh9BBgYdsJd6n4zxrape3olhRpgityb+FyZhvZreroQguJBeFO2tngGm875enT9lNdOfWn9XMxv
        H1b68LrU0h6OSPWed5KPyuq3w9/gh+JtS/EeOoY/xWDoyKayRYv3KtV6222gI1UZgfpm9rV0dlLnYQAR2YCTQe9jDkNscADAB
        EYLYLCUVaiSFaF45TuRCcn/KPeRBsCgQIIymvEc8h35XegoeoFPQxiAQa5whShNKctkmkNB8SEPfgxpSl5mKMOkeBBvkws
        LfEB4E4uQpAESAF9zBnwnvwYEBAA7""")

paremale_ikoon = PhotoImage(data = """
        R0lGODlhNgA2AHAAACH5BAEAAPwALAAAAAA2ADYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMw
        ArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqm
        QCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/z
        MrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOq
        ZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2
        YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZma
        qmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkr
        M5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5
        nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrz
        Mwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszV
        mczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9V
        zP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAA
        AAAAAAAAAAAAAj/ACf0mCCQ4MCCCA8qNMgwYcOFDhHeENhg4MQeFSdczLgRo8aPEzt+xGiRYsmFA1MWVMmyQY
        MbDF7GbGCjwYSKNlmu3FmSYsGMQAfibMDghoGjAJIaALAUBtEbNid+nCoVYsqMOi3GXJq0q9evBmLEvMhzZMayI29CZ
        RDAKwwtWxQtkqtoixYYXo++zOmQZU+SP2tyBaACDK1a5XSVI7e4sa5airR4JUqSo0SGOvcO1qKo3OJdjMmBHh161y5a
        kpW63JmWoNTXFLmqUAQ6sePPoW2TC10rNYCiOLOWxcigK5hapRkrFp28NulduhSpSHqAwcqcNguSfZl0du3l328v/9f
        dmPEivACgetRZVWb3ReOZ4ybPmJYi5M9310JvAOtZng0ckBR8tyk3H3OjvUVaeaeh55JCWH3UAFeKJEfeeLp8kxsteGkR
        3njSMaXeZULZkJQW5SwInoWKtVjOdABogZx45SiiFFRlQdUULQyyWKBj6MW4YGmpWUbQRwICQBuCpXljmze1MbkL
        jCfOyOR+TPHVw0EmAgCDhvNhGGZ5iVGZ1HHyKQdGUjgCBtWATNKYm5iKBdmVhxbWMp0BI2o0oZfxDYlblKB9oxiHX
        52oIjlrAoCVUEltYeByGubXGC1zgQGDCnZ+pQWP4y2SVExHwpQULVHaFh9uc22a6KuKTv863QE3HPSmCpZOahstYJg
        J66sy5ramAUURxEBTucUZ2jeKdPorrMe1SEhSOfVwQ6yCutjrs9x21Zl51Er15yLJDglZt+h+CxotImqXlLrMgamYjehySyB40
        5Hq0ruJyavbIr6+6uqviojJrqO1apRUGBYa6Kxb96H6MACL8GigaHgZcKQNS3W2Ym30vuqdYwErueJn9KqH0YkXkwwrDO
        TO5ywYnolJTi2jHvQnDHKKKvCMGPqqiIYnK9bogxoJqAKot/nm1WzlYuzVkqmOJ1l/ChUHQHj1PRzGoLxRed+cujUIAK3a
        NRDroCLTkiZu6C2paoF6MjUVRk31u1zIXoH/sQvYo00nN9lOitYoWUJdq2SyPn8FBtm5wTC4iqruiTRFWm/hoi4AE+a5CuQ
        SyhxkP75NThjh8vQmxcmiqgt00MnZ44fi7cmASj8pDgPTq7asa3xWzk3OFmxGJdB6RJ1ZtfC59jho4TWqFuFORhHmMZm+
        Vyql76Mhmp5/AKpNWOjbg31g2Wli+ZuW2rnmZ1KSk2mx6IW+TWdqtF7Fmkqrg+6ifP8bk8V0oz4+3UQnJjEIUcSnpOCJB
        nr/Ex3KYHQALRlJOKuL0b1kZzPQ9KYrB6gJYCAiEq1U70So4l7DThOy/rAvgVtKiAX3daeKcW0+mLpLV/j0EtyRpT0INCFSW
        brzFrlgShFy0YIOQdgm9+HuIAypSloSd4DBJCpgPLxdhEb4KMxMTyV7mZCArKiUKu5lfw9p30kAtMbKQAUqNYHKXpDHPxjy
        xYs+eSJaJmI8G2CGRNTjSUAAADs=""")

puhasta_ikoon = PhotoImage(data = """
        R0lGODlhNwA2AHAAACH5BAEAAPwALAAAAAA3ADYAhwAAAAAAMwAAZgAAmQAAzAAA/wArAA
        ArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wC
        qAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//z
        MAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zO
        AADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/z
        P/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAG
        ZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbV
        M2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZ
        krzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5
        nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8w
        rZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcy
        qzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
        M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qz
        P+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAAAj/AHtMmCCQ4MCCCA8Ov
        DGhQY8GDR9GnGiwYkKLCwk6nMDwoUCGIBs0uMGggY0DDGA0MMAgRskbEGF65KjxY02DAnPi3Gm
        wAQ+RJFeuvIFyZAMGEhPqXEpTo9OkMR0edQnAAICrWLNaNWAS6MSNGzEy1QmypNWsWFUEQMt
        WJdKNZG/SzBmzoVm0AWLgwPHjjZE3cPym8YHjxlqsVkVKHUtQJ1yaMG9oBdBgb44ifY30/YEDAdGsBw
        DYMHkQIkKIOwWOnMCgKtYAONL8gGOnNpw7cGjHsZ3bx48YWYeanluR4dyjkrHGuPHDDm3nuZ3bhj69
        N4DQV7mOPq20IUm0OOAY/3GO284R20ziwGFym30c9tL7Yq96YPVS1XQbuA5gIHz08bSJV54du0UnHR
        xNwCEbcFcdYIANGTVF1wQ2ZEWYHUyQp9uBdhgRIBO4bficeDHMd0BHFm3EwGcAwBadetIBmKCGB8I
        nY4B/MQjAinWRtdJVhdlR3noBcghgetIVeGCRcPxgwFralSZRAypd5UAMR35Y4Iy3FXkebUaU5yF8cBQRA
        AxVeZXQDWfF4NeGRqThQBodJlknkzX+wFwadwC411VsEgeTfkAyCccBwB3wQ3Ngcvglkj8UscJ1ii6JHVc
        ScSTBfIzaWCIAMfSl5G5h4tlkGqGpcMAbBf4VmlUoev93lgEeEghdAwyG1hyAHOrGBKrY4ToerzhgxQBNXW
        EVXozOFXHoaz/QWSp7My46XwxliniHpA3K1ANXWDX3noi5JXcdAIxy6KSOWNIYIByEcnWsSGhWRSeeux
        WhIwwBMFrebr8dBmqtYA5prkdshhZDAEUMOSOARtxQbLiNNjmfsB8WGebEoilmgFWI5oZkka0+mx1ndiya
        FbZF2NllfFiJ1ANRsN7Aa4BcHijxVWvhwN9VMbQLh5JEdohbEVgF9SMAMjTQJZnOjdxhDA5ktwJRKlyFMXpE
        w7wWAwfM/DFl/mkoddG5cbyyh+/2OmMcb/zskkhPAoBDDFCTrCGRJmP/tWqRCfZJIJnsIa31imxaVSJtjxbIH
        nzxnZUVDlFHZ6qtaWClUkMGJIqty/C1Wt4PWaM123hi2nobrz/EHNnYBxxAcOgH3uGcbwLPBwBhlg+Zd+uHe
        3yVCi13jXaTZwJ5Axx/trh7rQD+yx682ckUmbKNkqr6opI7TbAPkzugsZEMcmVcSeHWOL7KyvrVIfOTL6vkl3fE
        3WAPx74OdPQBjg5q0myTjh2KJTkcDKtXwAMADCYCE8nNpk7jStnklkebf40nBz4QWNlKFq/VFKdNBHPOog
        TmPQT9pzrgOwsOxAefH4CPMpgyCExaA7LcFMmFpbNbYPQ2NOi07jCFsRxn/64Cg7CZBi6xA5IPIPYpuy3P
        Q7ixEXpogwMfOJBIiDpchB5CEjalj4qtM6CBRESg8RAtB/2hXG4udgMU6UQjhLpOpALkrIrdaUYcKtC7HMAxAz
        DkMTLkSGuAFq0APdBXplpd5VImHjjsLDtwGU5HogKaH9SqV+66A5mG1KE39NF8E7nIR6YSPyiasXJ5q9Pgfj
        Mf8z1mJm7kCEosVDYt0SiCREOVuSizoi02RC4/gYlrGmRJy6mPRkbAjNoMcCL7pGYxDPTO0rJzAL5kppGN
        dOFeVKWVGTLmj0lJEY9WIrnXIApXiConYhRDHKlYBH/EmclH/MgW+pTongcQGGK6aFicsYDFMUuJilGGWU
        +0MNOVA7nJhOjCGEDaJDIjOejHHDTOyMiQKY8xjqBSE0j8vAQyHOmRlErD0YJEEiMgdQpIQhrSxeRPLB09
        olwYGk+OlpSjKIplSQMCADs=""")

painted_floor = PhotoImage(data = """
        R0lGODlhIAAgAPcAAAAAAAAABgAAHQAATAAAlgAA/wAEAAAEBgAEHQAETAAElgAE/wATAA
        ATBgATHQATTAATlgAT/wAxAAAxBgAxHQAxTAAxlgAx/wBhAABhBgBhHQBhTABhlgBh/wCm
        AACmBgCmHQCmTACmlgCm/wD/AAD/BgD/HQD/TAD/lgD//wYAAAYABgYAHQYATAYAlgYA/w
        YEAAYEBgYEHQYETAYElgYE/wYTAAYTBgYTHQYTTAYTlgYT/wYxAAYxBgYxHQYxTAYxlgYx
        /wZhAAZhBgZhHQZhTAZhlgZh/wamAAamBgamHQamTAamlgam/wb/AAb/Bgb/HQb/TAb/lg
        b//x0AAB0ABh0AHR0ATB0Alh0A/x0EAB0EBh0EHR0ETB0Elh0E/x0TAB0TBh0THR0TTB0T
        lh0T/x0xAB0xBh0xHR0xTB0xlh0x/x1hAB1hBh1hHR1hTB1hlh1h/x2mAB2mBh2mHR2mTB
        2mlh2m/x3/AB3/Bh3/HR3/TB3/lh3//0wAAEwABkwAHUwATEwAlkwA/0wEAEwEBkwEHUwE
        TEwElkwE/0wTAEwTBkwTHUwTTEwTlkwT/0wxAEwxBkwxHUwxTEwxlkwx/0xhAExhBkxhHU
        xhTExhlkxh/0ymAEymBkymHUymTEymlkym/0z/AEz/Bkz/HUz/TEz/lkz//5YAAJYABpYA
        HZYATJYAlpYA/5YEAJYEBpYEHZYETJYElpYE/5YTAJYTBpYTHZYTTJYTlpYT/5YxAJYxBp
        YxHZYxTJYxlpYx/5ZhAJZhBpZhHZZhTJZhlpZh/5amAJamBpamHZamTJamlpam/5b/AJb/
        Bpb/HZb/TJb/lpb///8AAP8ABv8AHf8ATP8Alv8A//8EAP8EBv8EHf8ETP8Elv8E//8TAP
        8TBv8THf8TTP8Tlv8T//8xAP8xBv8xHf8xTP8xlv8x//9hAP9hBv9hHf9hTP9hlv9h//+m
        AP+mBv+mHf+mTP+mlv///////////////////////////////////////////yH5BAAAAA
        AALAAAAAAgACAABwj/AAEoS0aPYLJkwxAWVDaP4cCCBRFKhAggWcODBjFaTDZwXsaMDA8+
        5OhxYcOGJjkmHHbxJMeCJUmGdLjSoMeBDg3OvHiwZsSbN0lm/NlxZNCIJh0CVSkx50WcHi
        UK7WnR6MGlDE+OtLm1qMyRTr1qlWkwZUiiG5OK9NiSY9qqVT3WtEk1YU6IOumtxOk24kiz
        WON2pIsXr9CQEhOSbdk1qNaLEWVGVXuxJmSMO0NeHirUpE+4C93OdXo4KMaUMMe6bOryLO
        eBOjeCXSp59mDAO0vDzj3QLmjdOiuzLh23LmnNGZfC5Iv4qmSSl++uzfrXKFRliJEeXO72
        8tPiifuGRh+mOWzdzTDJducbk+v2q7PfM274mSfS7GS5R4UqPmLCm6MFJZ12UuWEHFftrU
        SPasQd5dVW2nlFID0ArKYdVkBJ+B4AAQEAOw==""")
plain_floor = PhotoImage (data = """
        R0lGODlhIAAgAOf1AAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAA
        BVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDV
        AADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/z
        MrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
        /zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zD
        P//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZV
        zGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmW
        bVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkr
        mZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZp
        mqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wA
        ZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8
        yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/
        M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP
        9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///V
        AP/VM//VZv/Vmf/VzP///////////////////////////////////////////yH+EUNyZW
        F0ZWQgd2l0aCBHSU1QACwAAAAAIAAgAAAI/gABKEtGj2CyZMMQFlQ2j+HAggURSoQIIFnD
        gwYxWkw2cF7GjAwPPuTocWHDhiY5Jhx28STHgiVJhnS40qDHgQ4Nzrx4sGbEmzdJZvzZcW
        TQiCYdAlUpMedFnB4lCu1p0ejBpQxPjrS5tajMkU69apVpMGVIohuTivTYkmPaqlU91rRJ
        NWFOiDrprcTpNuJIs1jjdqSLF6/QkBITkm3ZNajWixFlRlV7sSZkjDtDXh4q1KRPuAvdzn
        V6OCjGlDDHumzq8izngTo3gl0qefZgwDtLw8490C5o3Torsy4dty5pzRmXwuSL+Kpkkpfv
        rs361yhUZYiRHlzu9vLT4on7R4Yfpjls3c0wyXbnG5Pr9quz3zNu+Jkn0uxkuUeFKj5iwp
        ujBSWddlLlhBxX7a1Ej2rEHeXVVtp5RSA9AKymHVZASfgeAAEBADs=""")
pykkar_e = PhotoImage (data = """
        R0lGODlhIAAgALMAAAAAAJ83G8febf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAACH5BAEAAAMALAAAAAAgACAAAwSMcMhJq7046827/6AWjKRXXmRaAagqAXCc
        sVY6DrGgCzIFiyTAbriL/X4bGHFJm/QsyqW0mRRKr1SMFWsscrY8Y5TnTV7JRWv2Aia21d
        8zOLqGytNlTXu47ddXezpdeU5sOWeESDNjWDhPFTYvgWEsipCRkkyAGJiSMS5Ofxw2AZsh
        pCGpqqusra6vFREAOw==""")
pykkar_n = PhotoImage (data = """
        R0lGODlhIAAgALMAAAAAAJ83G8febf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAACH5BAEAAAMALAAAAAAgACAAAwSecMhJq724grxp59N3fYCIbWU2pKkammPr
        SnA8a3PtdmXfh7dAgLYSGI8CX2eYEdIAyOhxI2RenEVkTwqoNofQaSkZRnoxznJSqxacr4
        HxlKvFotvt9XRgPUXlc3s5XEpqOhp0UkYyKoCLimQ3NH+QhyOUXJIeZXlJmnxCnWJvX2mQ
        nqRoXo5aoH2qWJ0pqaqbhRK0aJqvn72+v8DBwBEAOw==""")
pykkar_s = PhotoImage (data = """
        R0lGODlhIAAgALMAAAAAAJ83G8febf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAACH5BAEAAAMALAAAAAAgACAAAwSZcMhJq7046827/2DwiV1gSkCqptTJmWIq
        zLQASDCpwQNQ16zc6+T70W7CDUxmPPI+xV+UBeo1o7MbtGmTQrFAqXbDvBrHGuxKde6oxd
        6d9XiW6i6mtxQIcOFNcHRHA34WMGc+bIOFFUuIYFqMLURcfDh3higrVz2XbhNrKihVnWRV
        VKYeomRoaTeoFyytsWOzFLWpoBm2pCARADs=""")
pykkar_w = PhotoImage (data = """
        R0lGODlhIAAgALMAAAAAAJ83G8febf///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAACH5BAEAAAMALAAAAAAgACAAAwSJcMhJq7046827/2AIBmQpAkBVmuKAqiUq
        U2uAvRQg7Dw+1LbLS8YrCnC120xnNM40PldzKktZrLlidXrEZlC9MNd76zGP3COHCRZT17
        tzPE0WxuVyJ3x+r+L3XUR0gGladWWFZkpkeU1RSi5bdCtQjG19P0lXX34TmhVkQEEWLBxA
        LaipqqusIREAOw==""")
wall = PhotoImage (data = """
        R0lGODlhIAAgAIQAAAAAAGpsN2tVRWBgYHNzcwFhuCiX/owtALplDZlvQNl8ALqOV6quYv
        +1Us/RbYSEhJaWlrmoktWWhsa9lN+uot7Wrf/aqOvnkv//hMDAwMbGxtjY2AAAAAAAAAAA
        AAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQAZAAAACwAAAAAIAAgAIcAAAAAADMAAGYAAJ
        kAAMwAAP8AKwAAKzMAK2YAK5kAK8wAK/8AVQAAVTMAVWYAVZkAVcwAVf8AgAAAgDMAgGYA
        gJkAgMwAgP8AqgAAqjMAqmYAqpkAqswAqv8A1QAA1TMA1WYA1ZkA1cwA1f8A/wAA/zMA/2
        YA/5kA/8wA//8zAAAzADMzAGYzAJkzAMwzAP8zKwAzKzMzK2YzK5kzK8wzK/8zVQAzVTMz
        VWYzVZkzVcwzVf8zgAAzgDMzgGYzgJkzgMwzgP8zqgAzqjMzqmYzqpkzqswzqv8z1QAz1T
        Mz1WYz1Zkz1cwz1f8z/wAz/zMz/2Yz/5kz/8wz//9mAABmADNmAGZmAJlmAMxmAP9mKwBm
        KzNmK2ZmK5lmK8xmK/9mVQBmVTNmVWZmVZlmVcxmVf9mgABmgDNmgGZmgJlmgMxmgP9mqg
        BmqjNmqmZmqplmqsxmqv9m1QBm1TNm1WZm1Zlm1cxm1f9m/wBm/zNm/2Zm/5lm/8xm//+Z
        AACZADOZAGaZAJmZAMyZAP+ZKwCZKzOZK2aZK5mZK8yZK/+ZVQCZVTOZVWaZVZmZVcyZVf
        +ZgACZgDOZgGaZgJmZgMyZgP+ZqgCZqjOZqmaZqpmZqsyZqv+Z1QCZ1TOZ1WaZ1ZmZ1cyZ
        1f+Z/wCZ/zOZ/2aZ/5mZ/8yZ///MAADMADPMAGbMAJnMAMzMAP/MKwDMKzPMK2bMK5nMK8
        zMK//MVQDMVTPMVWbMVZnMVczMVf/MgADMgDPMgGbMgJnMgMzMgP/MqgDMqjPMqmbMqpnM
        qszMqv/M1QDM1TPM1WbM1ZnM1czM1f/M/wDM/zPM/2bM/5nM/8zM////AAD/ADP/AGb/AJ
        n/AMz/AP//KwD/KzP/K2b/K5n/K8z/K///VQD/VTP/VWb/VZn/Vcz/Vf//gAD/gDP/gGb/
        gJn/gMz/gP//qgD/qjP/qmb/qpn/qsz/qv//1QD/1TP/1Wb/1Zn/1cz/1f///wD//zP//2
        b//5n//8z///8AAAAAAAAAAAAAAAAI/wABAECjbBKaSWIATFJ28GDCgQUdKmRoEOHEimgS
        EsSYcCFHiB8pNuxY0WBCkSYVlsy48CBCMQnFjOxI8WXMmQoPZrrxUGBGmR1d9ug5EGZGAD
        DF8ASQSRlDgVCRwlza9GlUgTB9Eiup0SlSNFq5TvTK1GnDSUsjKhO4EGXas18xGpwIV6Zc
        sBvrTgrpsiHSvW5SRsQoNTCaTCf3ws14NrHLSW5iwnw5sGImiUkR4l1JeeDSv2cjPxQzFK
        tcmTmhXkZ6eW/W1WzBirmcFGTXvVKV3r49KTfYlhZbHsT6myJNNMOhEjwYGaLL5s4h8w5M
        U3HwwUc9Vjy+HUBEh0G3n5lsrJGjGOAIS593WHzk0fWaB+KEajRrQ8RE60sGWtZq1KSvmX
        WVTw+hsZVOXa111EAHToLYWGuNdVZaBkXY1oTjVRRXY3RpaBeHeXlo2VE1+QUfbd7dVZR1
        iclVFIeDKRbTUPGdBZlFQDFWWV/4YfUZfPPVBpp4TIEVG2suoTbXkbP9tNtEgeW2FEEPUt
        lbUu1ZFCKBHR6XXEAAOw==""")


vasakule_nupp = ttk.Button (raam, command=vasakule)
#vasakule_pilt = PhotoImage(file = "vasakule.gif")
vasakule_nupp.config(image=vasakule_ikoon)
vasakule_nupp.grid(column = 0, row = 0, padx = 5, pady = 5)

liigu_nupp = ttk.Button (raam, command=liigu)
#liigu_pilt = PhotoImage(file = "liigu.gif")
liigu_nupp.config(image=liigu_ikoon)
liigu_nupp.grid(column = 1, row = 0, padx = 5, pady = 5)

paremale_nupp = ttk.Button (raam, command=paremale)
#paremale_pilt = PhotoImage(file = "paremale.gif")
paremale_nupp.config(image=paremale_ikoon)
paremale_nupp.grid(column = 2, row = 0, padx = 5, pady = 5)

puhasta_nupp = ttk.Button (raam, command=puhasta)
#puhasta_pilt = PhotoImage(file = "puhasta.gif")
puhasta_nupp.config(image=puhasta_ikoon)
puhasta_nupp.grid(column = 0, row = 1, padx = 5, pady = 5)

start_nupp = ttk.Button (raam, command=start)
#start_pilt = PhotoImage(file = "start.gif")
start_nupp.config(image=start_ikoon)
start_nupp.grid(column = 2, row = 1, padx = 5, pady = 5)


käsud = Canvas(raam, height= 500, width=250, background="white")
käsud.grid(row=3, columnspan= 3, padx=5, pady=5)
maailm = Canvas(raam)
pykkar = maailm.create_image(0,0)
def create_world(labürint):
    global maailm
    global pykkar
    global ruudu_suurus
    global maailm_list
    #loome maailma
    #kustutame vana maailma
    maailm.destroy()

    #ridadeks
    maailm_list = labürint.split("\n")
    #kõrguse ja laiuse määramine
    maailma_kõrgus = len(maailm_list) *  ruudu_suurus
    maailma_laius = len(maailm_list[0]) * ruudu_suurus
    #Tahvli loomine
    maailm = Canvas(raam, height= maailma_kõrgus, width=maailma_laius, background="white")
    maailm.grid(row=0, column=3, rowspan = 4,  padx=5, pady=5, sticky = N,)
    #ridade joonistamine
    pilt = """"""
    x_pilt=0
    y_pilt=0
    global pykkari_suund
    global pykkar_x
    global pykkar_y
    for a in maailm_list:
        rida = a
        for b in rida:
                
            if b=="#":
            
                maailm.create_image(x_pilt, y_pilt, image=wall, anchor=NW)
            elif b== " " or b == "F":
            
                maailm.create_image(x_pilt, y_pilt, image=plain_floor, anchor=NW)

            elif b == ".":

                maailm.create_image(x_pilt, y_pilt, image=painted_floor, anchor=NW)
            elif b == ">":
                maailm.create_image(x_pilt, y_pilt, image=plain_floor, anchor=NW)
                pykkar=maailm.create_image(x_pilt, y_pilt, image=pykkar_e, anchor=NW)
                pykkari_suund = "e"
                pykkar_x=x_pilt
                pykkar_y=y_pilt
            # värskendame piltide asukohta
            x_pilt += ruudu_suurus
        x_pilt = 0
        y_pilt += ruudu_suurus

create_world(labürint)
raam.mainloop()



