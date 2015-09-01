DJOAuth2-ng
========

* Source code: https://github.com/vden/djoauth2-ng

What is DJOAuth2?
-----------------

Built on top of DJOauth2: https://github.com/Locu/djoauth2

DJOAuth2-ng is an implementation of a *almost whole* subset of the `OAuth 2`_
specification, which is described by the `OAuth Website`_ as

  An open protocol to allow secure authorization in a simple and standard
  method from web, mobile and desktop applications.


The goal of this implementation is to provide a well-structured Django
application that can be easily installed to add OAuth 2.0 provider capability to
existing projects. The official specification is broad, and allows for
many different ways for clients and servers to interact with each other. This
implementation is a secure subset of these interactions in order to make it as
easy as possible to reap the benefits of OAuth without having to struggle with
the more difficult parts of the spec.

OAuth, and this implementation, are best suited to solving the following
problems:

* Allowing for fine-grained API control — you want your users to choose which
  applications have access to their data.
* Acting as an authentication server, allowing other sites to "Log in with
  <your app>".


.. _`OAuth 2`: http://tools.ietf.org/html/rfc6749
.. _`OAuth website`: http://oauth.net/

