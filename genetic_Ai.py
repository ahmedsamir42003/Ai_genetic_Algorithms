import random

#fitness function to evluate fitness for each gene
def fintness(gene):
    x=(gene[0]+gene[1])-(gene[2]+gene[3])+(gene[4]+gene[5])-(gene[6]+gene[7])
    return x


#create cross using one point crossover on best_1 gene and best_2 gene
def cross(best_1,best_2):
    gene_1=best_1[:4]+best_2[4:]
    gene_2=best_1[4:]+best_2[:4]
    return [gene_1,gene_2]

#create mutation operator on best_1 gene and best_best_2 gene
def mutation(best_1):
    li=best_1.copy()
    li[random.randint(0,7)]=random.randint(0,9)
    return li

def work(pop,n):
    if n==100:
        print("the best solution after 100 iteration is :",pop[0])
        return
    dec={}

    #put all genes we have in dec where keys = values from fitness function and values = the gene
    for i in pop:
        dec[fintness(i)]=i

    #choose based of order the out put and choose best two gene from them
    best=sorted(dec.keys(),reverse=True)

    #create new gene based on mutation
    gene1=dec[best[0]]
    gene2=dec[best[1]]
    gene3=mutation(dec.pop(best[0]))
    gene4=mutation(dec.pop(best[1]))
    newpop=[gene1,gene2,gene3,gene4]
    print(newpop)
    work(newpop,n+1)

    # #create new gene based on cross
    # gene1=dec[best[0]]
    # gene2=dec[best[1]]
    # newgene=cross(gene1,gene2)
    # newpop=[gene1,gene2,newgene[0],newgene[1]]
    # print(newpop)
    # work(newpop,n+1)


if __name__=='__main__':
    inti_pop = [
[6, 5, 4, 1, 3, 5, 3, 2],
[8, 7, 1, 2, 6, 6, 0, 1],
[2, 3, 9, 2, 1, 2, 8, 5],
[4, 1, 8, 5, 2, 0, 9, 4]
    ]
    work(inti_pop,0)