#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kigo
Version  : 18.12.3
Release  : 5
URL      : https://download.kde.org/stable/applications/18.12.3/src/kigo-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/kigo-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/kigo-18.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kigo-bin = %{version}-%{release}
Requires: kigo-data = %{version}-%{release}
Requires: kigo-license = %{version}-%{release}
Requires: kigo-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
Kigo - Go board game by KDE
===========================
tbd.

%package bin
Summary: bin components for the kigo package.
Group: Binaries
Requires: kigo-data = %{version}-%{release}
Requires: kigo-license = %{version}-%{release}

%description bin
bin components for the kigo package.


%package data
Summary: data components for the kigo package.
Group: Data

%description data
data components for the kigo package.


%package doc
Summary: doc components for the kigo package.
Group: Documentation

%description doc
doc components for the kigo package.


%package license
Summary: license components for the kigo package.
Group: Default

%description license
license components for the kigo package.


%package locales
Summary: locales components for the kigo package.
Group: Default

%description locales
locales components for the kigo package.


%prep
%setup -q -n kigo-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551999187
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1551999187
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kigo
cp COPYING %{buildroot}/usr/share/package-licenses/kigo/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kigo/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang kigo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kigo

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kigo.desktop
/usr/share/config.kcfg/kigo.kcfg
/usr/share/icons/hicolor/128x128/apps/kigo.png
/usr/share/icons/hicolor/16x16/apps/kigo.png
/usr/share/icons/hicolor/22x22/apps/kigo.png
/usr/share/icons/hicolor/32x32/apps/kigo.png
/usr/share/icons/hicolor/48x48/apps/kigo.png
/usr/share/icons/hicolor/64x64/apps/kigo.png
/usr/share/kigo/games/Honinbo-51-5.sgf
/usr/share/kigo/games/Mehin-21-2.sgf
/usr/share/kigo/themes/default.desktop
/usr/share/kigo/themes/kigo_default.png
/usr/share/kigo/themes/kigo_default.svgz
/usr/share/kigo/themes/kigo_plain.png
/usr/share/kigo/themes/kigo_plain.svgz
/usr/share/kigo/themes/plain.desktop
/usr/share/kxmlgui5/kigo/kigoui.rc
/usr/share/metainfo/org.kde.kigo.appdata.xml
/usr/share/xdg/kigo-games.knsrc
/usr/share/xdg/kigo.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kigo/get-new-games.png
/usr/share/doc/HTML/de/kigo/hint.png
/usr/share/doc/HTML/de/kigo/index.cache.bz2
/usr/share/doc/HTML/de/kigo/index.docbook
/usr/share/doc/HTML/de/kigo/play-game.png
/usr/share/doc/HTML/de/kigo/setup-general.png
/usr/share/doc/HTML/de/kigo/setup-theme.png
/usr/share/doc/HTML/de/kigo/start-loaded-game.png
/usr/share/doc/HTML/de/kigo/start-new-game.png
/usr/share/doc/HTML/en/kigo/get-new-games.png
/usr/share/doc/HTML/en/kigo/hint.png
/usr/share/doc/HTML/en/kigo/index.cache.bz2
/usr/share/doc/HTML/en/kigo/index.docbook
/usr/share/doc/HTML/en/kigo/play-game.png
/usr/share/doc/HTML/en/kigo/setup-general.png
/usr/share/doc/HTML/en/kigo/setup-theme.png
/usr/share/doc/HTML/en/kigo/start-loaded-game.png
/usr/share/doc/HTML/en/kigo/start-new-game.png
/usr/share/doc/HTML/es/kigo/index.cache.bz2
/usr/share/doc/HTML/es/kigo/index.docbook
/usr/share/doc/HTML/et/kigo/index.cache.bz2
/usr/share/doc/HTML/et/kigo/index.docbook
/usr/share/doc/HTML/fr/kigo/get_new_games.png
/usr/share/doc/HTML/fr/kigo/hint.png
/usr/share/doc/HTML/fr/kigo/index.cache.bz2
/usr/share/doc/HTML/fr/kigo/index.docbook
/usr/share/doc/HTML/fr/kigo/play-game.png
/usr/share/doc/HTML/fr/kigo/setup-general.png
/usr/share/doc/HTML/fr/kigo/setup-theme.png
/usr/share/doc/HTML/fr/kigo/start-loaded-game.png
/usr/share/doc/HTML/fr/kigo/start-new-game.png
/usr/share/doc/HTML/it/kigo/index.cache.bz2
/usr/share/doc/HTML/it/kigo/index.docbook
/usr/share/doc/HTML/nl/kigo/index.cache.bz2
/usr/share/doc/HTML/nl/kigo/index.docbook
/usr/share/doc/HTML/pt/kigo/index.cache.bz2
/usr/share/doc/HTML/pt/kigo/index.docbook
/usr/share/doc/HTML/pt_BR/kigo/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kigo/index.docbook
/usr/share/doc/HTML/ru/kigo/get-new-games.png
/usr/share/doc/HTML/ru/kigo/hint.png
/usr/share/doc/HTML/ru/kigo/index.cache.bz2
/usr/share/doc/HTML/ru/kigo/index.docbook
/usr/share/doc/HTML/ru/kigo/play-game.png
/usr/share/doc/HTML/ru/kigo/setup-general.png
/usr/share/doc/HTML/ru/kigo/setup-theme.png
/usr/share/doc/HTML/ru/kigo/start-loaded-game.png
/usr/share/doc/HTML/ru/kigo/start-new-game.png
/usr/share/doc/HTML/sv/kigo/index.cache.bz2
/usr/share/doc/HTML/sv/kigo/index.docbook
/usr/share/doc/HTML/uk/kigo/get-new-games.png
/usr/share/doc/HTML/uk/kigo/hint.png
/usr/share/doc/HTML/uk/kigo/index.cache.bz2
/usr/share/doc/HTML/uk/kigo/index.docbook
/usr/share/doc/HTML/uk/kigo/play-game.png
/usr/share/doc/HTML/uk/kigo/setup-general.png
/usr/share/doc/HTML/uk/kigo/setup-theme.png
/usr/share/doc/HTML/uk/kigo/start-loaded-game.png
/usr/share/doc/HTML/uk/kigo/start-new-game.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kigo/COPYING
/usr/share/package-licenses/kigo/COPYING.DOC

%files locales -f kigo.lang
%defattr(-,root,root,-)

