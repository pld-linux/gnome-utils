Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.1.0
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-utils/%{name}-%{version}.tar.gz
Patch0:		gnome-utils-applnk.patch
Patch1:		gnome-utils-fixdistr.patch
Patch2:		gnome-utils-sparkle.patch
Patch3:		gnome-utils-DESTDIR.patch
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
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	jade
BuildRequires:	docbook-dsssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

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
%patch0 -p1 -b .wiget
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

gzip -9nf AUTHORS ChangeLog NEWS README

install gstripchart/gstripchart.conf $RPM_BUILD_ROOT%{_datadir}/gstripchart

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/*/*.desktop
%{_datadir}/applets/Monitors/*
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/gcolorsel
%{_datadir}/gfloppy
%dir %{_datadir}/gstripchart/
%config %{_datadir}/gstripchart/gstripchart.conf
