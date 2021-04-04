import paramiko
import time

start_time = time.time()

count_before = 0
count_after = 0

try:
    # Executa a conexao
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.222.22", username="pi", password="_Dev_654_123")
    print ("Tempo para a conexao")
    print("--- %s seconds ---" % (time.time() - start_time))
except:
    print ("Sua estacao esta desligada!")

# Verifica quais janelas já estavam abertas
output = ""
com = "export DISPLAY=:0 && wmctrl -l"
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(com)

ssh_stdout=ssh_stdout.readlines()

#print (ssh_stdout)
#print (com)
for line in ssh_stdout:
    output=output+line
    count_before = count_before + 1 
if output!="":
    print (output)
else:
    print ("There was no output for this command")

print ()

# Abre a nova janela:
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("export DISPLAY=:0 && chromium-browser")
#time.sleep(5)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("export DISPLAY=:0 && firefox-esr")
#time.sleep(5)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("export DISPLAY=:0 && wmctrl -ia 0x01400001")
#time.sleep(5)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("export DISPLAY=:0 && wmctrl -ia 0x01e00003")

#Aguarda a nova janela abrir
'''
exit_status = ssh_stdout.channel.recv_exit_status()
if exit_status == 0:
    print ("Programa aberto!")
else:
    print("Error", exit_status)
'''
while count_before >= count_after:
    # Volta a verificar as janelas abertas
    count_after = 0
    output = ""
    com = "export DISPLAY=:0 && wmctrl -l"
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(com)

    ssh_stdout=ssh_stdout.readlines()

    #print (ssh_stdout)
    #print (com)
    for line in ssh_stdout:
        output=output+line
        count_after = count_after + 1
    if output!="":
        print (output)
    else:
        print ("There was no output for this command")

# Fecha a conexao
print ("ssh succuessful. Closing connection")
ssh.close()
print ("Connection closed!")

print("--- %s seconds ---" % (time.time() - start_time))
