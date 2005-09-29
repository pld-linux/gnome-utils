Summary:	GNOME utility programs
Summary(ja):	GNOME ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╔в╔М╔╟╔И╔Ю╫╦
Summary(pl):	Programy u©ytkowe GNOME
Summary(ru):	Утилиты GNOME, такие как поиск файлов и калькулятор
Summary(uk):	Утил╕ти GNOME, так╕ як пошук файл╕в та калькулятор
Summary(zh_CN):	GNOMEс╕сцЁлпР╪╞
Name:		gnome-utils
Version:	2.12.0
Release:	2
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-utils/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	950148f8d30f23185fc3910b2b45d978
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
BuildRequires:	gnome-desktop-devel >= 2.10.0-2
BuildRequires:	gnome-panel-devel >= 2.10.0-2
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	hal-devel >= 0.4.7
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	gnome-vfs2 >= 2.10.0-2
Requires:	gtk+2 >= 2:2.6.4
Obsoletes:	gnome
Obsoletes:	gnome-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

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

%package dict
Summary:	Online dictionary
Summary(pl):	SЁownik online
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description dict
Allows to look up an online dictionary for definitions and correct
spellings of words.

%description dict -l pl
Pozwala na wyszukiwanie definicji i poprawnej pisowni sЁСw w sЁowniku
sieciowym.

%package floppy
Summary:	GNOME floppy formatter
Summary(pl):	Formater dyskietek dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description floppy
GFloppy formats floppy disks.

%description floppy -l pl
GFloppy formatuje dyskietki.

%package logview
Summary:	System log viewer for GNOME
Summary(pl):	Przegl╠darka logСw systemowych dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description logview
Allows to view system logs.

%description logview -l pl
Pozwala na przegl╠danie logСw systemowych.

%package search-tool
Summary:	GNOME search tool
Summary(pl):	NarzЙdzie wyszukuj╠ce dla GNOME
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description search-tool
Allows to search for files on system.

%description search-tool -l pl
Pozwala na wyszukiwanie plikСw w systemie.

%package screenshot
Summary:	Screenshot utility
Summary(pl):	NarzЙdzie do robienia zrzutСw ekranu
Group:		X11/Applications/Multimedia
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-utils <= 0:2.10.0-1

%description screenshot
Allows to make a desktop screenshot.

%description screenshot -l pl
Pozwala na zrobienie zrzutu ekranu biurka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gnome_doc_common}
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}-2.0
%find_lang gfloppy --with-gnome
%find_lang gnome-dictionary --with-gnome
%find_lang gnome-search-tool --with-gnome
%find_lang gnome-system-log --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post dict
%scrollkeeper_update_post
%gconf_schema_install gdict.schemas

%preun dict
%gconf_schema_uninstall gdict.schemas

%postun dict
%scrollkeeper_update_postun

%post floppy
%scrollkeeper_update_post
%update_desktop_database_post
%gconf_schema_install gfloppy.schemas

%preun floppy
%gconf_schema_uninstall gfloppy.schemas

%postun floppy
%scrollkeeper_update_postun
%update_desktop_database_postun

%post logview
%scrollkeeper_update_post
%gconf_schema_install logview.schemas

%preun logview
%gconf_schema_uninstall logview.schemas

%postun logview
%scrollkeeper_update_postun

%post search-tool
%scrollkeeper_update_post
%gconf_schema_install gnome-search-tool.schemas

%preun search-tool
%gconf_schema_uninstall gnome-search-tool.schemas

%postun search-tool
%scrollkeeper_update_postun

%post screenshot
%gconf_schema_install gnome-screenshot.schemas

%preun screenshot
%gconf_schema_uninstall gnome-screenshot.schemas

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade
%dir %{_omf_dest_dir}/%{name}

%files dict -f gnome-dictionary.lang
%defattr(644,root,root,755)
%doc gdictsrc/ChangeLog gdictsrc/README
%attr(755,root,root) %{_bindir}/gnome-dictionary
%attr(755,root,root) %{_libdir}/gdict-applet
%{_sysconfdir}/gconf/schemas/gdict.schemas
%{_desktopdir}/gnome-dictionary.desktop
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_mandir}/man1/gnome-dictionary*
%{_omf_dest_dir}/%{name}/gnome-dictionary-C.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gnome-dictionary-ja.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gnome-dictionary-uk.omf

%files floppy -f gfloppy.lang
%defattr(644,root,root,755)
%doc gfloppy/AUTHORS gfloppy/ChangeLog gfloppy/NEWS gfloppy/README gfloppy/TODO
%attr(755,root,root) %{_bindir}/gfloppy
%{_sysconfdir}/gconf/schemas/gfloppy.schemas
%{_desktopdir}/gfloppy.desktop
%{_datadir}/%{name}/glade/gfloppy2.glade
%{_mandir}/man1/gfloppy*
%{_omf_dest_dir}/%{name}/gfloppy-C.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gfloppy-ja.omf
%lang(nl) %{_omf_dest_dir}/%{name}/gfloppy-nl.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gfloppy-uk.omf

%files logview -f gnome-system-log.lang
%defattr(644,root,root,755)
%doc logview/ChangeLog logview/TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_sysconfdir}/gconf/schemas/logview.schemas
%{_desktopdir}/gnome-system-log.desktop
%{_datadir}/gnome-system-log
%{_mandir}/man1/gnome-system-log*
%{_omf_dest_dir}/%{name}/gnome-system-log-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/gnome-system-log-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/gnome-system-log-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gnome-system-log-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnome-system-log-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gnome-system-log-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gnome-system-log-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gnome-system-log-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gnome-system-log-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gnome-system-log-zh_CN.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gnome-system-log-zh_TW.omf

%files search-tool -f gnome-search-tool.lang
%defattr(644,root,root,755)
%doc gsearchtool/AUTHORS gsearchtool/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-search-tool
%{_sysconfdir}/gconf/schemas/gnome-search-tool.schemas
%{_desktopdir}/gnome-search-tool.desktop
%{_datadir}/%{name}
%{_mandir}/man1/gnome-search-tool*
%{_omf_dest_dir}/%{name}/gnome-search-tool-C.omf
%{_pixmapsdir}/gsearchtool
%lang(es) %{_omf_dest_dir}/%{name}/gnome-search-tool-es.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gnome-search-tool-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gnome-search-tool-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gnome-search-tool-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gnome-search-tool-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gnome-search-tool-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gnome-search-tool-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gnome-search-tool-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/gnome-search-tool-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gnome-search-tool-zh_TW.omf

%files screenshot
%defattr(644,root,root,755)
%doc gnome-screenshot/ChangeLog
%attr(755,root,root) %{_bindir}/gnome-panel-screenshot
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_sysconfdir}/gconf/schemas/gnome-screenshot.schemas
%{_datadir}/gnome-screenshot
