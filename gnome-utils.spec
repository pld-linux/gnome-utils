Summary:	GNOME utility programs
Summary(ja):	GNOME �桼�ƥ���ƥ��ץ���ླྀ
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	������� GNOME, ����� ��� ����� ������ � �����������
Summary(uk):	���̦�� GNOME, ��˦ �� ����� ���̦� �� �����������
Summary(zh_CN):	GNOMEӦ�ó���
Name:		gnome-utils
Version:	2.1.3
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	gnome-panel-devel >= 2.1.0
BuildRequires:	gnome-vfs2-devel >= 2.0.4-3
BuildRequires:	libbonoboui-devel >= 2.1.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.0.4
BuildRequires:	libgnomeui-devel >= 2.0.5
BuildRequires:	popt-devel
BuildRequires:	scrollkeeper >= 0.3.11
Requires:	gnome-vfs2 >= 2.1.3
Prereq:		scrollkeeper
Prereq:		GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnome-admin

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2
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

%build
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

mv ChangeLog main-ChangeLog
%find_lang %{name} --with-gnome --all-name
find . -name ChangeLog |awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); print "cp " src " " dst}'|sh

%post
/usr/bin/scrollkeeper-update
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS *ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/gdict-applet
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/%{name}
%{_datadir}/gnome-system-log
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
