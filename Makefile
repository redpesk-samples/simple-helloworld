DESTDIR ?=
PREFIX ?= /usr

helloworld:
	$cc main.c -o helloworld

install: helloworld
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 helloworld $(DESTDIR)$(PREFIX)/bin
