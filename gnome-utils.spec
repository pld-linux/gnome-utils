Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.0.50
Release:	1
Copyright:	LGPL
Group:		X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Patch0:		gnome-utils-applnk.patch
Patch1:		gnome-utils-automake.patch
Patch2:		gnome-utils-gstripchart_help.patch
Icon:		gnome-utils.gif
URL:		http://www.gnome.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	libgtop-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_applnkdir	%{_datadir}/applnk
%define		_localstatedir	/var

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment.  That's a fancy
name but really GNOME is a nice GUI desktop environment.  It makes
using your computer easy, powerful, and easy to configure.

%description -l pl
Programy u¿ytkowe GNOME'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
automake
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/*.desktop
%{_applnkdir}/*/*.desktop
%{_datadir}/pixmaps/*

%dir %{_datadir}/gnome/help/ghex
%{_datadir}/gnome/help/ghex/C
%lang(es) %{_datadir}/gnome/help/ghex/es
%lang(sv) %{_datadir}/gnome/help/ghex/sv

%dir %{_datadir}/gnome/help/gshutdown
%{_datadir}/gnome/help/gshutdown/C
%lang(es) %{_datadir}/gnome/help/gshutdown/es
%lang(no) %{_datadir}/gnome/help/gshutdown/no

%dir %{_datadir}/gnome/help/gstripchart
%{_datadir}/gnome/help/gstripchart/C

%dir %{_datadir}/gnome/help/gtt
%{_datadir}/gnome/help/gtt/C
%lang(de) %{_datadir}/gnome/help/gtt/de
%lang(es) %{_datadir}/gnome/help/gtt/es
