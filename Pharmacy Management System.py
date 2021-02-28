from tkinter import *
import time
import random
global fh




def new():
    global medicine, moreinfo, phone
    medicine = medicineentry.get()
    moreinfo = moreinfoentry.get()
    phone = (phoneentry.get())
    fh = open('Registers.txt', 'a')
    fh.write(f'Phone Number : {phone}\n')
    fh.write(f'First Name : {firstname}\n')
    fh.write(f'Last Name : {lastname}\n')
    fh.write(f'Token Number : {tokennumber}\n')
    fh.write(f'Date : {clock}\n')
    fh.write(f'Age : {age}\n')
    fh.write(f'Weight : {weight}\n')
    fh.write(f'Height : {height}\n')
    fh.write(f'Issue : {issue}\n')
    fh.write(f'Doctor : {doctor}\n')
    fh.write(f'Job : {job}\n')
    fh.write(f'Address : {address}\n')
    fh.write(f'Medicine : {medicine}\n')
    fh.write(f'More Info : {moreinfo}\n\n\n')
    fh.close()

    screen4.destroy()
    screen3.destroy()
    screen2.destroy()


def prescription():
    global screen4, medicineentry, moreinfoentry, phoneentry
    screen4 = Toplevel(screen)
    screen4.geometry("750x700")
    screen4.title("Prescription")
    Label(screen4, text=f"Prescription", font=("Brush MT Script", 25, UNDERLINE)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"First Name: {firstname}", font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"Last Name: {lastname}", font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"Token Number: {tokennumber}", font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"Health Issue: {issue}", font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"Medicine : ", font=("Brush MT Script", 17)).pack()
    medicineentry = Entry(screen4, font=("Brush MT Script", 13))
    medicineentry.pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Label(screen4, text=f"More Info : ", font=("Brush MT Script", 17)).pack()
    moreinfoentry = Entry(screen4, font=("Brush MT Script", 17))
    moreinfoentry.pack()
    Button(screen4, text="Return To Main Page", command=new, width = 20, height=2, font=("Brush MT Script", 17)).pack()
    Label(screen4, text="", font=("Brush MT Script", 17)).pack()
    Button(screen4, text="Quit", command=lambda: quit(), width=20, height=2, font=("Brush MT Script", 17)).pack()
# 1231002462552622115124560106833022683302241118121010017320231462863132310631283142031711631631631052602992313145253316412317602431324414255032361829926024112131629017220181012312201002961210025921310172960101612416476832824003200312810324932701910132800279027802770102622800279027802770103120327015280027902780277027602750102642801210312032701710028001026226902700271028002790278027702760280010312132701423702120100280010265280010312532701423702360101228001026528001031253270132370236010132800102652800103126327002370236010142800102652800103126237121015280010265280010312523702360237010152710102572800279027801015280010312523601002370102602800279027802770101726902700271028002790278027701031212370102602790102132800103124237010319923701028526802690270027102800103109237010289280010319928001031992800103199280010319927002710102422370236023502410103195237023601013241010319223712236010132410103193237121015241010318922802370236023502370101424101031912370101222802370236014132410103190237010132370241122700271028001031902370101323712236010319323701013237010319523701013228010319523601046028261010313626101031961300010217261010226180103118001023419010019121024218010246317901031052100190100190210010242180102463179010310621001001901024119123100019121024431790101231790102210010244191210019121023219010019010241210019031000190210010242318112318303181123183031811210264191210019021001026918010171903100019010243318112318303181123183031810318201021719121001912102432100100190102181800010250180101719031000210010244318203183031811231830318201014180102131912100191210243190100190102161912310001912102472100190310001902100102523182031830318212318303182010121912310001912102121901001901026319123100019121024719123100019021001025331820101231820101319123100019121021421001026419031000190102491903100019010262190310001901028019031000190102491903100019010262190310002100105113533301262385622721337867972708079013673708485326927831092303112010224103402317131024398510100512016101031034379110101451337410101351202610100512741101005123111010051210610101251344510101251187110103100443841010310043795101031004458110101451284110101012422426833022012320031281031991512103116228023702360235010278151210311723701028015121031172370102802131210311723701028021312103117237010233327001013327001024221312103117228023701021128012102173270191024021312103118237010142800279027802770276027502740273026902710280027901021532701910239213121031222790278010192800241014162280237023602350101232701410122120280032701310240151210313327101002411723701021127102800327014102381512103134241022302240225022602270228023702360102122710280010032701210239150103141237010214270027101003270010238150103141237023601016327016102442161210313923702360101832701910240216121031362370236023502340102123270151024121612103135237023601026121600010313423702360103197237023601026400102182370236023501031102360235023401028423701031042370228023702360102912370103103237023601002370102732130102182370103103237010122370102732130102182370103102237023601012237010272213121021823701031022360101323701023123602350234023302320231023002290102342130102182370103106237010292237010319922702280103378141210319914010319814121031981412103198141210319814121031981412103198141210421981401031991401037991401032440121031970131031970121031541701024201310319624100141031950141031962410103199241010163144151031500010237241010141313313414131410219180101531790101218010311531811210031810102360010142591332641425914100001000010000102111912310001902100100318112318303181121801022331790102913182031810101231810102121801022731210247022001014220025002510312101021721001903100019121003182031810318303181031820180102213181123183031811210173179010282318201003182010140141015180102273120010193120010218190310001901013318103183031820190310001912102193182031810318303181031820101731790102173179010264318101021518010227259010192590102182100310001901013318203183031810190310001902100102203181031830318101016318203181031830318103182010212180101231790102653182010212191231000191210225259032440101732450259010225318201001903100019010221318203183031810101631820318103183031811210210191231000191231830318112102762100190310001912102252592111022721003100021001022231820101831810318303181010211191231000190210031830318103182010277210031000190102983182031830318201021219031000190318103183031810102781903100021001029931820102132100310001903182031830318201031983182010511661330126341756227213378679727080790136737084853269278310923031120102241034023189135122631010145127341010051207810103100512234101013512734101031035122621010135120761010310051208410101351279110101251279410101351293710100512068101005116021010310051208010103100512294101010

def hospital():
    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("1350x750+0+0")
    screen3.title("Hospital Management System")
    screen2.destroy()
    Label(screen3, text="Hospital Management System", font=("Brush MT Script", 30)).grid(row=1, column=5)
    Label(screen3, text=f"First Name : {firstname}", font=("Brush MT Script", 17)).grid(row=3, column=2)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=4, column=2)
    Label(screen3, text=f"Last Name : {lastname}", font=("Brush MT Script", 17)).grid(row=5, column=2)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=6, column=2)
    Label(screen3, text=f"Date : {clock}", font=("Brush MT Script", 17)).grid(row=7, column=2)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=8, column=2)
    Label(screen3, text=f"Token Number : {tokennumber}", font=("Brush MT Script", 17)).grid(row=9, column=2)
    Label(screen3, text=f"Age : {age}", font=("Brush MT Script", 17)).grid(row=2, column=5)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=3, column=5)
    Label(screen3, text=f"Weight : {weight}", font=("Brush MT Script", 17)).grid(row=4, column=5)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=5, column=5)
    Label(screen3, text=f"Height : {height}", font=("Brush MT Script", 17)).grid(row=6, column=5)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=7, column=5)
    Label(screen3, text=f"Issue : {issue}", font=("Brush MT Script", 17)).grid(row=8, column=5)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=3, column=8)
    Label(screen3, text=f"Doctor : {doctor}", font=("Brush MT Script", 17)).grid(row=4, column=8)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=5, column=8)
    Label(screen3, text=f"Job : {job}", font=("Brush MT Script", 17)).grid(row=6, column=8)
    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=7, column=8)
    Label(screen3, text=f"Address : {address}", font=("Brush MT Script", 17)).grid(row=8, column=8)

    Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=9, column=5)
    Button(screen3, text="Prescription", command = prescription, width = 20, height=3, font=("Brush MT Script", 17)).grid(row=10, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=11, column=5)
    #Label(screen3, text=f"Prescription", font=("Brush MT Script", 25)).grid(row=12, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=13, column=5)
    #Label(screen3, text=f"Date: {clock}", font=("Brush MT Script", 17)).grid(row=14, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=15, column=5)
    #Label(screen3, text=f"First Name: {firstname}", font=("Brush MT Script", 17)).grid(row=16, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=17, column=5)
    #Label(screen3, text=f"Second Name: {lastname}", font=("Brush MT Script", 17)).grid(row=18, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=19, column=5)
    #Label(screen3, text=f"Token Number: {tokennumber}", font=("Brush MT Script", 17)).grid(row=20, column=5)
    #Label(screen3, text="", font=("Brush MT Script", 17)).grid(row=21, column=5)
    #Label(screen3, text=f"Issue : {issue}", font=("Brush MT Script", 17)).grid(row=22, column=5)
    #Entry(screen3, font=("Brush MT Script", 25)).grid(row=23, column=5)



def reset():
    screen2.destroy()
    register()

def token():
    global l1, l2, l3, tokennumber, firstname, lastname, age, weight, height, issue, doctor, job, address
    tokennumber = random.randint(2000,4000)
    firstname = str(firstnameentry.get())
    lastname = str(lastnameentry.get())
    age = ageentry.get()
    height = heightentry.get()
    weight = weightentry.get()
    issue = str(issueentry.get())
    doctor = start.get()
    job = jobentry.get()
    address = addressentry.get()
    l1 =Label(screen2, text=f"Name : {firstname} {lastname}", font=("Brush MT Script", 17)).grid(row=3, column=5)
    l2 =Label(screen2, text=f"Token Number : {tokennumber}", font=("Brush MT Script", 17)).grid(row=5, column=5)
    l3 =Label(screen2, text=f"Please Meet {doctor}", font=("Brush MT Script", 17)).grid(row=7, column=5)
    Button(screen2, text=f"Meet {doctor}", command=hospital, width=15, height=2, font=("Brush MT Script", 17)).grid(row=9,
                                                                                                        column=5)




def register():
    global screen2, firstnameentry, lastnameentry, ageentry, heightentry, weightentry, issueentry, doctormenu, start, jobentry, addressentry
    screen2 = Toplevel(screen)
    screen2.geometry("1350x750+0+0")
    screen2.title("Pharmacy Management System")
    Label(screen2, text="Registration Management System", font=("Brush MT Script", 30)).grid(row=1, column=5)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=2, column=1)
    Label(screen2, text="First Name: ", font=("Brush MT Script", 17)).grid(row=3, column=1)
    firstnameentry = Entry(screen2)
    firstnameentry.grid(row=3, column=2)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=4, column=1)
    Label(screen2, text="Last Name: ", font=("Brush MT Script", 17)).grid(row=5, column=1)
    lastnameentry = Entry(screen2)
    lastnameentry.grid(row=5, column=2)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=6, column=1)
    Label(screen2, text="Age : ", font=("Brush MT Script", 17)).grid(row=7, column=1)
    ageentry = Entry(screen2)
    ageentry.grid(row=7, column=2)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=8, column=1)
    Label(screen2, text="Height(cm) : ", font=("Brush MT Script", 17)).grid(row=9, column=1)
    heightentry = Entry(screen2)
    heightentry.grid(row=9, column=2)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=10, column=1)
    Label(screen2, text="Weight(kg) : ", font=("Brush MT Script", 17)).grid(row=11, column=1)
    weightentry = Entry(screen2)
    weightentry.grid(row=11, column=2)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=12, column=1)
    Label(screen2, text="Job : ", font=("Brush MT Script", 17)).grid(row=13, column=1)
    jobentry = Entry(screen2)
    jobentry.grid(row=13, column=2)


    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=3, column=4)
    Label(screen2, text="Health Issue : ", font=("Brush MT Script", 17)).grid(row=3, column=6)
    issueentry = Entry(screen2, width=50)
    issueentry.grid(row=3, column=7)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=4, column=5)
    Label(screen2, text="Doctors : ", font=("Brush MT Script", 17)).grid(row=5, column=6)
    start = StringVar()
    start.set("Choose A Doctor ...")
    doctormenu = OptionMenu(screen2, start, "Dr John", "Dr Mathews", "Dr Abraham", "Dr Tim", "Dr Fred", "Dr Bob", "Dr Robinson")
    doctormenu.grid(row=5, column=7, padx = 25, pady = 25)
    Label(screen2, text="", font=("Brush MT Script", 17)).grid(row=6, column=7)
    Label(screen2, text="Address : ", font=("Brush MT Script", 17)).grid(row=7, column=6)
    addressentry = Entry(screen2)
    addressentry.grid(row=7, column=7)
    Button(screen2, text="Token", command = token, width = 15, height=2, font=("Brush MT Script", 17)).grid(row=12, column=5)
    Button(screen2, text="Reset", command=reset, width=15, height=2, font=("Brush MT Script", 17)).grid(row=14,
                                                                                                        column=5)

def main_screen():
    global screen,clock
    screen = Tk()
    screen.geometry("600x400")
    screen.title("Pharmacy Management System")
    clock = time.asctime(time.localtime(time.time()))
    Label(screen, text="Pharmacy Management System", bg="gray"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text=f"Time : {clock}", width=300
          , height=2, font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Create New Appointment", command=register, height=3
           , width=40, font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Quit",command=lambda: quit(), height=3
           , width=40, font=("Brush MT Script", 13)).pack()

    screen.mainloop()

main_screen()
