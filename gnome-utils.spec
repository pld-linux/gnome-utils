Summary:	GNOME utility programs
Summary(ja):	GNOME ユーティリティプログラム集
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	�塢棉壅 GNOME, 堊防� 冒� 佻瓶� 徳別�� � 冒蒙釦妄塹�
Summary(uk):	�塢巳塢 GNOME, 堊胞 冕 佻柎� 徳別ψ 堊 冒蒙釦妄塹�
Summary(zh_CN):	GNOME哘喘殻會鹿
Name:		gnome-utils
Version:	1.4.1.3
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-utils/1.4/%{name}-%{version}.tar.gz
# Source0-md5:	75fe3acdb134cfa27c04ac3ab4581b6a
Patch0:		%{name}-am_fixes.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-am_conditional.patch
Patch3:		%{name}-defs.patch
Patch4:		%{name}-omf.patch
Patch5:		%{name}-ac.patch
Patch6:		%{name}-desktop.patch
Patch7:		%{name}-bogus_dir.patch
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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

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
