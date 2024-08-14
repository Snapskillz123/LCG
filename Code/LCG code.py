from Crypto.Util.number import long_to_bytes, bytes_to_long
# Function to generate random numbers
def linearCongruentialMethod(Xo, m, a, c, randomNums,noOfRandomNums):

	# Initialize the seed state
	randomNums[0] = Xo

	# Traverse to generate required
	# numbers of random numbers
	for i in range(1, noOfRandomNums):
		
		# Follow the linear congruential method
		randomNums[i] = ((randomNums[i - 1] * a) +c) % m
		

# Driver Code
if __name__ == '__main__':
	
	# Seed value
	Xo = 5
	
	# Modulus parameter
	m = 33914684861748025775039281034732118800210172226202865626649257734640860626122496857824722482435571212266837521062975265470108636677204118801674455876175256919094583111702086440374440069720564836535455468886946320281180036997133848753476194808776154286740338853149382219104098930424628379244203425638143586895732678175237573473771798480275214400819978317207532566320561087373402673942574292313462136068626729114505686759701305592972367260477978324301469299251420212283758756993372112866755859599750559165005003201133841030574381795101573167606659158769490361449603797836102692182242091338045317594471059984757228202609971840405638858696334676026230362235521239830379389872765912383844262135900613776738814453
	
	# Multiplier term
	a = 693066931880848926558533826475645982933482275070097717749629
	
	# Increment term
	c = 5901547799381070840359392038174495588170513247847714273595411167296183629412915012222227027356430642556122066895371444948863326101566394976530551223412292667644441453331065752759544619792554573114517925105448879969399346787436142706971884168511458472259984991259195488997495087540800463362289424481986635322685691583804462882482621269852340750338483349943910768394808039522826196641550659069967791745064008046300108627004744686494254057929843770761235779923141642086541365488201157760211440185514437408144860842733403640608261720306139244013974182714767738134497204545868435961883422098094282377180143072849852529146164709312766146939608395412424617384059645917698095750364523710239164016515753752257367489

	# Number of Random numbers
	# to be generated
	noOfRandomNums = 10

	# To store random numbers
	randomNums = [0] * (noOfRandomNums)

	# Function Call
	linearCongruentialMethod(Xo, m, a, c,randomNums, noOfRandomNums)

	# Print the generated random numbers
	for i in randomNums:
		print(i,",")
'''
print(bytes_to_long(b"niteCTF{th1s_15_tH3_fL4g}"))
'''



