DESTDIR ?=
PREFIX ?= /usr
LIBEXECDIR ?= /usr/libexec
PKGNAME ?= simple-helloworld
CC ?= gcc

helloworld:
	$(CC) main.c -o helloworld

install: helloworld
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin $(DESTDIR)$(LIBEXECDIR)/redtest/$(PKGNAME)
	install -m 0755 helloworld $(DESTDIR)$(PREFIX)/bin
	install -m 0755 redtest/run-redtest $(DESTDIR)$(LIBEXECDIR)/redtest/$(PKGNAME)
