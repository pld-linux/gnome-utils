Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.0.51
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-utils/%{name}-%{version}.tar.gz
Patch0:		gnome-utils-applnk.patch
Patch1:		gnome-utils-fixdistr.patch
Patch2:		gnome-utils-sparkle.patch
Patch3:		gnome-utils-DESTDIR.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	ncurses-devel >= 5.0
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

GNOME is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your computer
easy, powerful, and easy to configure.

%description -l pl
Programy u¿ytkowe GNOME'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
automake
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gstripchart

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README

install gstripchart/gstripchart.conf $RPM_BUILD_ROOT%{_datadir}/gstripchart

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
%{_datadir}/applets/Monitors/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/gstripchart/
%config %{_datadir}/gstripchart/gstripchart.conf

%dir %{_datadir}/gnome/help/gdiskfree
%{_datadir}/gnome/help/gdiskfree/C

%dir %{_datadir}/gnome/help/gfontsel
%{_datadir}/gnome/help/gfontsel/C

%dir %{_datadir}/gnome/help/gsearchtool
%{_datadir}/gnome/help/gsearchtool/C

%dir %{_datadir}/gnome/help/gshutdown
%lang(en) %{_datadir}/gnome/help/gshutdown/C
%lang(es) %{_datadir}/gnome/help/gshutdown/es
%lang(no) %{_datadir}/gnome/help/gshutdown/no

%dir %{_datadir}/gnome/help/gstripchart
%{_datadir}/gnome/help/gstripchart/C

%dir %{_datadir}/gnome/help/gtt
%{_datadir}/gnome/help/gtt/C
%lang(de) %{_datadir}/gnome/help/gtt/de
%lang(es) %{_datadir}/gnome/help/gtt/es
