# CSF
System that scan code.

What is the point of this project?

The programers of today are lazy and wanting to work on the good stuff. However, 
the reality is that we need secure system and sometimes the programer not acknowledge that he have unsecure code!!

So, our solution is to give the programer the ability to download extension in vscode and it will scan is code in real time and notify him about unsecure code in his own code and the programer will get a suggestion how to fix the problem.

## Architect:

This is going to be a microservice architect that going to run on k8s.

Why I chose this architect?

First, this system should have a lot of functionality, so, if I chose monolithic architect I assume that as the system grows, we will find a struggle in increasing system capabilities. 

Second, when we use microservice we will have a better performance for high data capacity, since, 
every microservice is responsible for his own task and it is not dependent on another microservice.

Third, this approach is better for design this kind of system, because, we will need to develope many
engines that responsible for each scan, so, if we make them all dependent on each other we will see how the
process of the scanning is getting slower.


What we need to do now?

- create issues
- research
- design