Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.4.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-utils/%{name}-%{version}.tar.gz
Patch0:		%{name}-fixdistr.patch
Patch1:		%{name}-sparkle.patch
Patch2:		%{name}-errordialog.patch
Patch3:		%{name}-configure.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	ORBit-devel
BuildRequires:	bonobo-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	esound-devel
BuildRequires:	gdbm-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	jade
BuildRequires:	docbook-style-dsssl
BuildRequires:	flex
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnome-admin

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Programy u¿ytkowe GNOME'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
gettextize --copy --force
automake -a -c
aclocal -I macros
autoconf
gettextize --copy --force
(cd gfloppy; gettextize --copy --force)
%configure

%{__make} LIBS="-ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gstripchart

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	Utilitiesdir=%{_applnkdir}/Utilities \
	gdictappdir=%{_applnkdir}/Utilities \
	Systemdir=%{_applnkdir}/System \
	Productivitydir=%{_applnkdir}/Applications \
	desktopdir=%{_applnkdir}/Utilities 

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/*/*.desktop
%{_datadir}/applets/*/*
%{_datadir}/idl/*
%{_pixmapsdir}/*
%{_datadir}/mime-info/*
%{_datadir}/gcolorsel
%{_datadir}/logview
%{_datadir}/%{name}
%{_datadir}/omf/%{name}
%dir %{_datadir}/stripchart/
%config %{_datadir}/stripchart/stripchart.conf
%{_datadir}/stripchart/stripchart.params
