
def getHint(secret: str, guess: str) -> str:
    secret_ls = [i for i in secret]
    guess_ls = [i for i in guess]
    a,b = 0,0
    for x in range(len(secret_ls)):
        if secret_ls[x] in guess_ls:
            if guess_ls[x] == secret_ls[x]:
                guess_ls[x] = "-1"
                secret_ls[x] = "-2"
                a+=1
    for x in range(len(secret_ls)):
        if secret_ls[x] in guess_ls:
            if guess_ls[x] != secret_ls[x]:
                guess_ls[guess_ls.index(secret_ls[x])] = "-1"
                b+=1
    #return "{}A{}B".format(a,b)
    print("a = ",a," b = ",b)

getHint("1807","7810")