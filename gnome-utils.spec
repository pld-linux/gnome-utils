Summary:	GNOME utility programs
Summary(ja):	GNOME ユーティリティプログラム集
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	�塢棉壅 GNOME, 堊防� 冒� 佻瓶� 徳別�� � 冒蒙釦妄塹�
Summary(uk):	�塢巳塢 GNOME, 堊胞 冕 佻柎� 徳別ψ 堊 冒蒙釦妄塹�
Summary(zh_CN):	GNOME哘喘殻會鹿
Name:		gnome-utils
Version:	2.6.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	522cd062e1f3e516390ae61fda2a5f55
Patch0:		%{name}-kdev_t.patch
Patch1: 	%{name}-locale-names.patch
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	gnome-desktop-devel >= 2.6.1
BuildRequires:	gnome-panel-devel >= 2.6.1
BuildRequires:	gnome-vfs2-devel >= 2.6.1.1
BuildRequires:	intltool >= 0.29
BuildRequires:	libbonoboui-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgnome-devel >= 2.6.1
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	gnome-vfs2 >= 2.6.1.1
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

mv po/{no,nb}.po

%build
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
