Summary:	GNOME utility programs
Summary(ja):	GNOME ユーティリティプログラム集
Summary(pl):	Programy u�ytkowe GNOME
Summary(ru):	�塢棉壅 GNOME, 堊防� 冒� 佻瓶� 徳別�� � 冒蒙釦妄塹�
Summary(uk):	�塢巳塢 GNOME, 堊胞 冕 佻柎� 徳別ψ 堊 冒蒙釦妄塹�
Summary(zh_CN):	GNOME哘喘殻會鹿
Name:		gnome-utils
Version:	1.106.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	xmldocs.make
Source2:	omf.make
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	GConf2-devel
BuildRequires:	gnome-panel-devel >= 1.5.21
BuildRequires:	gnome-vfs2-devel >= 1.9.3
BuildRequires:	libbonoboui-devel >= 1.116.0
BuildRequires:	libglade2-devel >= 1.99.2
BuildRequires:	libgnome-devel >= 1.117.0
BuildRequires:	libgnomeui-devel >= 1.117.0
BuildRequires:	popt-devel
BuildRequires:	scrollkeeper
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

%build
install -m644 %{SOURCE1} xmldocs.make
install -m644 %{SOURCE2} omf.make
rm -f missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--disable-console-helper \
	--enable-gdialog

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%post
/usr/bin/scrollkeeper-update
GCONF_CONFIG_SOURCE="" %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/%{name}
%{_datadir}/idl/*
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
