Summary:	GNOME utility programs
Summary(ja):	GNOME ユーティリティプログラム集
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	�塢棉壅 GNOME, 堊防� 冒� 佻瓶� 徳別�� � 冒蒙釦妄塹�
Summary(uk):	�塢巳塢 GNOME, 堊胞 冕 佻柎� 徳別ψ 堊 冒蒙釦妄塹�
Summary(zh_CN):	GNOME哘喘殻會鹿
Name:		gnome-utils
Version:	2.10.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-utils/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	43644d28321645aa68428e99fadb2504
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-omf.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	gnome-panel-devel >= 2.10.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0
BuildRequires:	hal-devel >= 0.4.7
BuildRequires:	intltool >= 0.31.3
BuildRequires:	libglade2-devel >= 1:2.5.0
BuildRequires:	libgnomeprintui-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.10.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	gnome-vfs2 >= 2.10.0
Requires:	gtk+2 >= 2:2.6.2
Obsoletes:	gnome
Obsoletes:	gnome-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l ja
GNOME (GNU Network Object Model Environment) は、 X Window System の
ウィンドウマネージャと協調して動くユーザフレンドリーな GUI
アプリケーション とデスクトップツール集です。 gnome-utils
パッケージは、 GNOME の ユーティリティ集です。
Gcalc,Gdialog,Gdiskfree, そしてその他 いろいろなツールが含まれます。

%description -l pl
Programy u�ytkowe GNOME'a.

%description -l ru
�塹� 仭謀� 嗜津雙不 療墨塹燮� 孕斌不� 通� GNOME, 堊防� 冒� 瀕嘖簒妖淋
通� 佻瓶冒 徳別��, 冒蒙釦妄塹�, 凖珍穆碗 16-夘淮惑� 墨珍 � �.�.

%description -l uk
稘� 仭謀� 勇嘖不� 津冕� 孕斌υ� 通� GNOME, 堊胞 冕 ξ嘖簒妖淋 通�
佻柎釦 徳別ψ, 冒蒙釦妄塹�, 凖珍穆碗 16-墨從馬 墨蔦, 塹殤.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/gnome-common/data/omf.make .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%post
umask 022
/usr/bin/scrollkeeper-update
%gconf_schema_install
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

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
%{_datadir}/gnome-screenshot
%{_datadir}/gnome-system-log
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
