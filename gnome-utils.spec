Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.0.1
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org
Icon:		%{name}.gif
Requires:	gtk+ >= 1.2.0, glib >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

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
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--localstatedir=/var

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*
/usr/X11R6/share/gnome/apps/Applications/*
/usr/X11R6/share/gnome/apps/Settings/*
/usr/X11R6/share/gnome/apps/Utilities/*
/usr/X11R6/share/gnome/apps/*.desktop
/usr/X11R6/share/gnome/help/*
/usr/X11R6/share/gstripchart/*
/usr/X11R6/share/pixmaps/*
