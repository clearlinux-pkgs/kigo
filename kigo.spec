#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kigo
Version  : 23.04.0
Release  : 52
URL      : https://download.kde.org/stable/release-service/23.04.0/src/kigo-23.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.0/src/kigo-23.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.0/src/kigo-23.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 GPL-3.0
Requires: kigo-bin = %{version}-%{release}
Requires: kigo-data = %{version}-%{release}
Requires: kigo-license = %{version}-%{release}
Requires: kigo-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kigo-23.04.0
cd %{_builddir}/kigo-23.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682091270
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1682091270
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kigo
cp %{_builddir}/kigo-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kigo/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kigo-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kigo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kigo-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kigo/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kigo-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kigo/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kigo-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kigo/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kigo-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kigo/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/kigo-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kigo/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kigo-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kigo/7d9831e05094ce723947d729c2a46a09d6e90275 || :
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
/usr/share/knsrcfiles/kigo-games.knsrc
/usr/share/knsrcfiles/kigo.knsrc
/usr/share/metainfo/org.kde.kigo.appdata.xml
/usr/share/qlogging-categories5/kigo.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kigo/index.cache.bz2
/usr/share/doc/HTML/ca/kigo/index.docbook
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
/usr/share/package-licenses/kigo/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kigo/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kigo/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kigo/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kigo/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kigo/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kigo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f kigo.lang
%defattr(-,root,root,-)

