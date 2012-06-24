Summary:     GNOME utility programs
Summary(pl): Programy u�ytkowe GNOME
Name:        gnome-utils
Version:     0.28
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Obsoletes:   gnome
URL:         http://www.gnome.org
BuildRoot:   /tmp/%{name}-%{version}-root

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Programy u�ytkowe GNOME'a 

%prep
%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=/usr
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
fi

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/share/apps/Applications/*
/usr/share/apps/Productivity/*
/usr/share/apps/System/*
/usr/share/apps/Utilities/*
/usr/share/apps/*.desktop
/usr/share/gnome/help/*
/usr/share/go
/usr/share/pixmaps/*
%lang(cs) /usr/share/locale/cs/LC_MESSAGES/gnome-utils.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnome-utils.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/gnome-utils.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnome-utils.mo
%lang(ga) /usr/share/locale/ga/LC_MESSAGES/gnome-utils.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnome-utils.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/gnome-utils.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/gnome-utils.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/gnome-utils.mo

%changelog
* Thu Sep  3 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.28-1]
- added -q %setup parameter,
- added pl translation (Wojtek �lusarczyk <wojtek@shadow.eu.org>),
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/gnome-utils.mo
  files.

* Mon Apr 6 1998 Marc Ewing <marc@redhat.com>
- Integrate into gnome-utils CVS source tree
