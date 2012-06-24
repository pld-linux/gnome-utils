Summary:	GNOME utility programs
Summary(ja):	GNOME �桼�ƥ���ƥ��ץ���ླྀ
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	������� GNOME, ����� ��� ����� ������ � �����������
Summary(uk):	���̦�� GNOME, ��˦ �� ����� ���̦� �� �����������
Summary(zh_CN):	GNOMEӦ�ó���
Name:		gnome-utils
Version:	1.4.1.2
Release:	5
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-utils/1.4/%{name}-%{version}.tar.gz
# Source0-md5:	02bd79a6c5d7f89c2485f3a4258d22fd
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-am_conditional.patch
Patch3:		%{name}-defs.patch
Patch4:		%{name}-omf.patch
Patch5:		%{name}-ac.patch
Patch6:		%{name}-desktop.patch
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
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	openjade
BuildRequires:	libglade-gnome-devel >= 0.11
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

%description -l ja
GNOME (GNU Network Object Model Environment) �ϡ� X Window System ��
������ɥ��ޥ͡�����ȶ�Ĵ����ư���桼���ե��ɥ꡼�� GUI
���ץꥱ������� �ȥǥ����ȥåץġ��뽸�Ǥ��� gnome-utils
�ѥå������ϡ� GNOME �� �桼�ƥ���ƥ����Ǥ���
Gcalc,Gdialog,Gdiskfree, �����Ƥ���¾ ������ʥġ��뤬�ޤޤ�ޤ���

%description -l pl
Programy u�ytkowe GNOME'a.

%description -l ru
���� ����� �������� ��������� ������� ��� GNOME, ����� ��� ����������
��� ������ ������, �����������, �������� 16-������� ���� � �.�.

%description -l uk
��� ����� ͦ����� ���˦ ���̦�� ��� GNOME, ��˦ �� ���������� ���
������ ���̦�, �����������, �������� 16-������ ����, ����.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--with-messages=/var/log/messages

%{__make} LIBS="-ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	Utilitiesdir=%{_applnkdir}/Utilities \
	gdictappdir=%{_applnkdir}/Utilities \
	Systemdir=%{_applnkdir}/System \
	Productivitydir=%{_applnkdir}/Utilities \
	desktopdir=%{_applnkdir}/Utilities \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
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
%{_omf_dest_dir}/%{name}
