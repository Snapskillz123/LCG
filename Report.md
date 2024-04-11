# LCG (Linear Congruential Generator)

  # Introduction
  LCG is a type of Pseudorandom number generator where numbers are generated within a specific range.
  
  It is called pseudorandom and not random because at the end of the day there is an arithmetic procedure to generate the numbers.

  # Math behind LCG
  It follows the formula:

  ![image](https://github.com/Snapskillz123/LCG/assets/149099858/1184b621-6241-43cb-81d6-cecdb3ca4646)

  First, a seed value should be chosen, and then an 'm' (modulus) value and the according a and c values.

  By using this formula on a loop, we generate different numbers that are technically random.

  We can also generate a bit sequence by doing mod 2 of the generated numbers.
  
  The equation resembles linear congruence which is of the form:

  ![image](https://github.com/Snapskillz123/LCG/assets/149099858/e01d6992-0a34-4df3-851b-a224de4a7a79)

  but what exactly is congruence?
  
  # Congruence and Linear Congruence
  
  Congruence is an integral part of modular arithmetic.

  You may see an expression like:

  ![image](https://github.com/Snapskillz123/LCG/assets/149099858/c659b35f-b320-4d89-ab13-38d61f73845f)

  This says that A is congruent to B modulo C.

  The three lines are the symbol of congruence

  Here's an example:
  
  ![image](https://github.com/Snapskillz123/LCG/assets/149099858/ffafc168-0432-4e60-92a5-7c1c6ed5bcd7)

  26-11 is congruent with 0(mod 5) and hence this equation is congruent because 15 mod 5 is 0.

  # Parameters for LCG

  When m is prime (usually Mersenne primes) and c is zero the encryption works but it is less efficient as it has to follow extra steps.

  When m in a power of two (usually 2^32 or 2^64) and c=0 the modulus operation becomes very simple.

  

  

 
 

  



  
