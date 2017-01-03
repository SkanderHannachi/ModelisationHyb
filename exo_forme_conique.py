import numpy as np 
import matplotlib.pyplot as plt 
import math as mth
#Definition des alpha beta 

alpha = lambda ls : max(ls)
beta  = lambda ls : min(ls)  
#Definition des fonctions 
cube  = lambda x  : x * x * x 
F     = lambda h  : -(0.2 * mth.sqrt(20*h))/ 3*cube(h)
G     = lambda h  : (0.2*mth.sqrt(20*h))/h 
E     = lambda h  : 1/(3*cube(h))
def F_ls(ls) : 
	"""Pour calculer les valeurs de la fonction F en chaque point """
	ll = []
	for i in range(len(ls)) : 
		ll.append(F(ls[i]))
	return ll  
def G_ls(ls) : 
	ll = []
	for i in range(len(ls)) : 
		ll.append(G(ls[i]))
	return ll
def E_ls(ls) : 
	ll = []
	for i in range(len(ls)) : 
		ll.append(E(ls[i]))
	return ll

#Calcul des fonction F' et F'' 

def F_1(ls) : 
	"""Retourne une liste """ 
	out=[]	
	for i in range(len(ls)) : 
		out.append((F(ls[i]) - beta(F_ls(ls)))/(alpha(F_ls(ls))-beta(F_ls(ls))))
	return out
def F_2(ls) : 
	out=[]	
	for i in range(len(ls)) : 
		out.append((alpha(F_ls(ls)) - F(ls[i]))/(alpha(F_ls(ls))-beta(F_ls(ls))))
	return out

def G_1(ls) : 
	out=[]	
	for i in range(len(ls)) : 
		out.append((G(ls[i]) - beta(G_ls(ls)))/(alpha(G_ls(ls))-beta(G_ls(ls))))
	return out

def G_2(ls) : 
	out=[]	
	for i in range(len(ls)) : 
		out.append((alpha(G_ls(ls)) - F(ls[i]))/(alpha(G_ls(ls))-beta(G_ls(ls)))	)
	return out

def E_1(ls) : 
	out=[]	
	for i in range(len(ls)) : 
		out.append((E(ls[i]) - beta(E_ls(ls)))/(alpha(E_ls(ls))-beta(E_ls(ls))))
	return out

def E_2(ls) : 
	out=[]	
	for i in range(len(ls)) : 
		out.append((alpha(E_ls(ls)) - E(ls[i]))/(alpha(E_ls(ls))-beta(E_ls(ls))))
	return out

def mu(l1,l2,l3) : 
	out=[]	
	for i in range(len(l1)) : 
		out.append(l1[i]*l2[i]*l3[i])
	return out

def main() : 
	x   = 0.01
	y   = 1.25 
	pas = 0.01 	
	L   = np.arange(x,y,pas)	
	Ls  = L.tolist()	
	f   = F_ls(Ls)
	g   = G_ls(Ls)
	e   = E_ls(Ls)			
	mu_1 = mu(F_1(Ls),G_1(Ls),E_1(Ls))	
	mu_2 = mu(F_1(Ls),G_1(Ls),E_2(Ls))	
	mu_3 = mu(F_1(Ls),G_2(Ls),E_1(Ls))	
	mu_4 = mu(F_1(Ls),G_2(Ls),E_2(Ls))	
	mu_5 = mu(F_2(Ls),G_1(Ls),E_1(Ls))	
	mu_6 = mu(F_2(Ls),G_1(Ls),E_2(Ls))	
	mu_7 = mu(F_2(Ls),G_2(Ls),E_1(Ls))	
	mu_8 = mu(F_2(Ls),G_2(Ls),E_2(Ls))	
	print(mu_2)	
	#return 0


#############################PP
if __name__ == "__main__" : 
	main() 


