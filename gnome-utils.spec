Summary:	GNOME utility programs
Summary(pl):	Programy u¿ytkowe GNOME
Name:		gnome-utils
Version:	1.4.1.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-utils/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-am_conditional.patch
Patch3:		%{name}-defs.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bonobo-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:	e2fsprogs-devel
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	gdbm-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	jade
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	oaf-devel >= 0.6.5
BuildRequires:	readline-devel
BuildRequires:	scrollkeeper
BuildRequires:	zlib-devel
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnome-admin

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure

%{__make} LIBS="-ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	Utilitiesdir=%{_applnkdir}/Utilities \
	gdictappdir=%{_applnkdir}/Utilities \
	Systemdir=%{_applnkdir}/System \
	Productivitydir=%{_applnkdir}/Utilities \
	desktopdir=%{_applnkdir}/Utilities \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_applnkdir}/*/*.desktop
%{_datadir}/application-registry
%{_datadir}/applets/*/*
%{_datadir}/gcolorsel
%{_datadir}/gnome-utils
%{_datadir}/gtt
%{_datadir}/idl/*
%{_datadir}/logview
%{_datadir}/mime-info/*
%{_mandir}/man*/*
%{_datadir}/stripchart
%{_pixmapsdir}/*
%{_omf_dest_dir}/omf/%{name}
