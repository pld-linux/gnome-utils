Summary:	GNOME utility programs
Summary(ja):	GNOME ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╔в╔М╔╟╔И╔Ю╫╦
Summary(pl):	Programy u©ytkowe GNOME
Summary(ru):	Утилиты GNOME, такие как поиск файлов и калькулятор
Summary(uk):	Утил╕ти GNOME, так╕ як пошук файл╕в та калькулятор
Summary(zh_CN):	GNOMEс╕сцЁлпР╪╞
Name:		gnome-utils
Version:	2.3.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
Icon:		gnome-utils.xpm
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	gnome-panel-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	popt-devel
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	rpm-build >= 4.1-10
Requires:	gnome-vfs2 >= 2.2.0
Prereq:		scrollkeeper
Prereq:		GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome
Obsoletes:	gnome-admin

%define		_localstatedir	/var

%description
GNOME utility programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l ja
GNOME (GNU Network Object Model Environment) ╓о║╒ X Window System ╓н
╔╕╔ё╔С╔и╔╕╔ч╔м║╪╔╦╔Ц╓х╤╗д╢╓╥╓фф╟╓╞╔Ф║╪╔╤╔у╔Л╔С╔и╔Й║╪╓й GUI
╔╒╔в╔Й╔╠║╪╔╥╔Г╔С ╓х╔г╔╧╔╞╔х╔ц╔в╔д║╪╔К╫╦╓г╓╧║ё gnome-utils
╔я╔ц╔╠║╪╔╦╓о║╒ GNOME ╓н ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╫╦╓г╓╧║ё
Gcalc,Gdialog,Gdiskfree, ╓╫╓╥╓ф╓╫╓нб╬ ╓╓╓М╓╓╓М╓й╔д║╪╔К╓╛╢ч╓ч╓Л╓ч╓╧║ё

%description -l pl
Programy u©ytkowe GNOME'a.

%description -l ru
Этот пакет содержит некоторые утилиты для GNOME, такие как инструмент
для поиска файлов, калькулятор, редактор 16-ричного кода и т.п.

%description -l uk
Цей пакет м╕стить деяк╕ утил╕ти для GNOME, так╕ як ╕нструмент для
пошуку файл╕в, калькулятор, редактор 16-кового коду, тощо.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

mv ChangeLog main-ChangeLog
%find_lang %{name} --with-gnome --all-name
find . -name ChangeLog |awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst); print "cp " src " " dst}'|sh

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
