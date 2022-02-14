from ast import literal_eval
import typing
from memory_class import memory_sim
#This program handles the commands and cli
#It does not contain simulation code however

print_strings_source_file="sim_main_strings.txt"

def main():
    initialize()
    parameters=load_sim()
    #sim_loop(parameters)
    #handle_final_exit()
    print("exiting lol")



def initialize():
    banner()
    initialization_loop()



def banner():
    print_str("banner")



def initialization_loop():
    loop_done=False
    print_str("init_start")
    counter=0
    counter_bound=4
    while loop_done==False:
        if counter==0:
            print_str("init_loop_default")
        counter=counter+1
        counter=counter%counter_bound
        terminal_input=input(">")
        line=extract_input(terminal_input)
        if line==[]:
            pass
        elif len(line)==1: 
            command=line[0]
            arguments=None
        else:
            command=line[0]
            arguments=line[1]
        if command=="help" :
            if arguments==None:
                init_help("1")
            elif len(arguments)==1:
                num=str(arguments[0])
                init_help(num)
            else:
                print_str("init_help_error")
        elif command=="license":
            if arguments!=None:
                print_str("init_license_error")
            else:
                print_str("init_license")
        elif command=="continue":
            if arguments!=None:
                print_str("init_continue_error")
            else:
                print_str("init_continue")
                loop_done=True
        else:
            print_str("init_unknown_command")



def init_help(num):
    if num==None:
        print_str("init_help")
    try:
        a=int(num)
        if a>=1 and a<=3:
            print_str("init_help_"+num)
        else:
            print_str("init_help_error")
    except:
        print_str("init_help_error")



def load_sim():
    loop_done=False
    print_str("load_sim_start")
    register_names=["PC","SP",  #see specs
                                "GP_1","GP_2","GP_3","GP_4",
                                "GP_5","GP_6","GP_7","GP_8",
                                "GP_9","GP_10","GP_11","GP_12",
                                "GP_13","GP_14","GP_15","GP_16",]
    memory_address_width=64 #64 bit width as per specs
    registers=memory_sim(register_names,"list")
    memory=memory_sim(memory_address_width,"address width")
    while loop_done==False:
        terminal_input=input(">")
        print("lol IDK smthg")  #incorrect, do some things
            #load from file mem+register
            #don't forget file extension stuff
            #also bypass mode
            #and help
            #note that if one wants to do direct memory/reg read write, suggest in help using the bypass mode
        loop_done=True
    parameters=(registers,memory) #given the way this program handles memory, empty dicts that represent registers and memories is a valid option that starts the program in a null state
    return(parameters)




def print_str(target:str):
    #the file should be a dict() and targets/snippets should have the accompanying keys
    with open(print_strings_source_file,"r") as file:
        full_file=file.read()
        strings=literal_eval(full_file)
        print(strings[target])




def extract_input(terminal_input:str):
    temp_1=list()
    temp_1=terminal_input.split()
    if temp_1==[]:
        return(None)
    elif len(temp_1)==1:
        return(temp_1)
    else:
        temp_2=["dummy_content"]
        temp_2[0]=(temp_1[0])
        temp_2.append(temp_1[1:len(temp_1)])
        return(temp_2)

        

if __name__=="__main__":    #boring boiler plate for making things easier for others
    main()