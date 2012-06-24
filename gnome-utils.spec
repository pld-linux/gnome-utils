Summary:	GNOME utility programs
Summary(ja):	GNOME �桼�ƥ���ƥ��ץ���ླྀ
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	������� GNOME, ����� ��� ����� ������ � �����������
Summary(uk):	���̦�� GNOME, ��˦ �� ����� ���̦� �� �����������
Summary(zh_CN):	GNOMEӦ�ó���
Name:		gnome-utils
Version:	2.5.90
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	bd7e193525cf2053b3588328cbe855ed
Patch0:		%{name}-kdev_t.patch
Patch1: 	%{name}-locale-names.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.90
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnome-panel-devel >= 2.5.91
BuildRequires:	gnome-vfs2-devel >= 2.5.90
BuildRequires:	libbonoboui-devel >= 2.5.3
BuildRequires:	libglade2-devel >= 2.3.2
BuildRequires:	libgnome-devel >= 2.5.90
BuildRequires:	libgnomeui-devel >= 2.5.90
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post):	scrollkeeper
Requires(post):	GConf2
Requires:	gnome-vfs2 >= 2.5.90
Obsoletes:	gnome
Obsoletes:	gnome-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var

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

mv po/{no,nb}.po

%build
%{__autoconf}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

mv ChangeLog main-ChangeLog
find . -name ChangeLog |awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); print "cp " src " " dst}'|sh

%find_lang %{name} --with-gnome --all-name

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS *ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/gdict-applet
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/%{name}
%{_datadir}/gnome-system-log
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
