Title: What is microservices?
Date: 2017-02-06 15:15
Modified: 2017-02-06 15:15
Category: Microservices
Tags: distributed, thoughts, microservice
Authors: Vlad Calin
Illustration: 3-cover.jpeg

The title is a reference to the famous *"What is drugs?"* news footage that is out there on the internet (if you don't know it, you can view it
[here](https://youtu.be/kan_FWhjrMw?t=37s)).

So, what is microservice?

I am sure that you heard this term and wondered why everybody is talking about it. What is it? What is it good for? What problems does this solve?

In this article I am going to write a little about this phenomenon that is supposed to change the world (and currently does).

So, what is a microservice?
===========================

A microservice is... well... a service ... that is small... and does things... and is webscale... and... whatever....

Joking aside, a microservice is a stand-alone service (application) that provides simple and independent functionality for a larger system. By simple and independent functionality I want to say that it is responsible in managing a single kind of information/entities (users, subscriptions, notifications, etc) or as fewer as possible. 

A larger system that is developed by using a microservice architecture is composed from a number of independent microservices that communicate with each other over the network. Such systems can be scaled (horizontaly) more easily, can handle failiures, does not need huge investments in performant hardware.

With this architecture, there appear multiple problems that must be handled:

- how do these services communicate with each other? How does this affect performance? What happens when the network fails?
- how do these services find out about each other?
- with multiple instances of the same service, how can I balance the load more efficiently?
- how do I handle security?
- many others :(

These questions are natural but they involve a broader discussion and I am not going to cover these aspects, at least not now.

What is it good for?
====================

As I said earlier, the major advantage in this architectural design is that we can scale better and easier horizontally and we can handle failiure more efficiently.

Scalability
-----------

Having a single service instance that handles all the operations resulted from user requests, over time, becomes more stressed as more users come and they are more active. So the initial situation looks something like this: we have a single service that handles all the requests. You can check some benchmarks for your favourite web framework to see how many requests per second it can handle before having problems and cause some performance issues. 

Availability
------------

Failure is handled in this manner: you have a number of instances of each service running. There are no two instances of the same service that run on the same node. In this case, let's assume that one node violently dies and everything on it stops working. You lose an instance of your service, but the other running instances can handle the requests that the dead one would normally handle! This is good news because all request are processed! And the chances that more nodes fail at the same time and leaves you with no running instance to handle the requests is very low.

Independend deployment
----------------------

Another advantage of the microservice pattern is that each service can be independently deployed. When a service needs to be updated, each instance can be updated at a time so that there will be no downtime, and also it is way faster than deploying a whole monolithic application. Of course, you have to be extra cautious to not screw up the communication between services as they need to continue to communicate with each other.

Technologies
------------

Because microservies run independently and they only interact via some inter-process communication methods, there are no technological restrictions for each microservice. Each microservice an be written in whatever language you want and what technology stack you want to use. It is no problem. All that matters is that the communication protocol between microservices to be well documented and robust.

But all this microservice thing is too hard!
============================================

Of course, an application that is structured in microservices is harder to maintain than a traditional monolithic application. With the advantages this pattern comes with, of course there are some disadvantages.

DevOps skills required
----------------------

In the traditional monolithic architecture is a single application, a single database, a single node and a few processes to monitor and manage. But in the microservice architecture, multiply it by the number of services and the number of nodes you have. There will be a lot of things to keep your eyes on and manage. Imagine that each microservice uses its own database, that is of different kind (one uses MySQL, one uses PostgreSQL, one uses MongoDB and so on) and some guys have to make sure that everything is working as expected. 

And as the application grows and more microservices are added and as more and more users use that application, there will be a lot more things to handle and things can go messy very easy.

Latency
-------

Because each microservice runs independently, eventually on multiple nodes, they need to communicate. What in the classic monolithic architecture every communication between two "services" are simple function calls, but in the microservice architecture, every call becomes a request (be it HTTP, message over AMQP, or some custom protocol over sockets). If a service takes more than a few microseconds to respond, that response time is added to the total response time of the original request and things can become messy: requests take too much time to get a response, the whole system lags, some service invokations might timeout and if they are not handled properly, there might occur some data loss, users get bored while they wait for the system to do its job, etcetera, etcetera.


Conclusion
==========

The microservice based architecture provides a method to develop applications that are very decoupled and can be easily scaled so that it fits our needs. But we must also be aware that this design also has flaws and, despite it advantages, we must think twice before using this pattern because it also comes with some flaws.

I recommend taking a look over [microservices.io](http://microservices.io/index.html) to read some more design patterns regarding this topic.
