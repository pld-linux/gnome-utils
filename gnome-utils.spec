Summary:     GNOME utility programs
Summary(pl): Programy u¿ytkowe GNOME
Name:        gnome-utils
Version:     0.30
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org
Icon:        %{name}.gif
Requires:    gtk+ >= 1.1.2, glib >= 1.1.3
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Programy u¿ytkowe GNOME'a 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root,  man) /usr/X11R6/man/man1/*
/usr/X11R6/share/apps/Applications/*
/usr/X11R6/share/apps/Productivity/*
/usr/X11R6/share/apps/System/*
/usr/X11R6/share/apps/Utilities/*
/usr/X11R6/share/apps/*.desktop
/usr/X11R6/share/gnome/help/*
/usr/X11R6/share/pixmaps/*
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/gnome-utils.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-utils.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-utils.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-utils.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-utils.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-utils.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-utils.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-utils.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-utils.mo

%changelog
* Fri Sep 25 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-1]
- added in Requires "gtk+ >= 1.1.2, glib >= 1.1.3",
- removed obsolete /usr/X11R6/share/go from main package.

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-2]
- added package Icon,
- changed prefix to /usr/X11R6.

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-1]
- added -q %setup parameter,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/gnome-utils.mo
  files.

* Mon Apr 6 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-utils CVS source tree
