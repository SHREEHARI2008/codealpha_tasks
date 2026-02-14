input_file=input("Enter input file name: ")
output_file=input("Enter output file name: ")
def extract_email():
    try:
        f=open(input_file,"r")
        data=f.readlines()
        if(f==None){
            
        f1=open(output_file,"w")
        for i in data:
            f1.write(i)
        f.close()
        f1.close()
        return
    except:
        printf("Error in handling file")
        return
    
        


