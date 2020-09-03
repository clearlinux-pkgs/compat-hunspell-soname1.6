#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-hunspell-soname1.6
Version  : 1.6.2
Release  : 6
URL      : https://github.com/hunspell/hunspell/archive/v1.6.2.tar.gz
Source0  : https://github.com/hunspell/hunspell/archive/v1.6.2.tar.gz
Summary  : Hunspell spellchecking library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MPL-1.1
Requires: compat-hunspell-soname1.6-lib = %{version}-%{release}
Requires: compat-hunspell-soname1.6-license = %{version}-%{release}
BuildRequires : bison

%description
About Hunspell
==============
NOTICE: Version 2 is in the works. For contributing see
[version 2 specification][v2spec] and the folder `src/hunspell2`.

%package lib
Summary: lib components for the compat-hunspell-soname1.6 package.
Group: Libraries
Requires: compat-hunspell-soname1.6-license = %{version}-%{release}

%description lib
lib components for the compat-hunspell-soname1.6 package.


%package license
Summary: license components for the compat-hunspell-soname1.6 package.
Group: Default

%description license
license components for the compat-hunspell-soname1.6 package.


%prep
%setup -q -n hunspell-1.6.2
cd %{_builddir}/hunspell-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599168737
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1599168737
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6
cp %{_builddir}/hunspell-1.6.2/COPYING %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/hunspell-1.6.2/COPYING.LESSER %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/hunspell-1.6.2/COPYING.MPL %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/aba8d76d0af67d57da3c3c321caa59f3d242386b
cp %{_builddir}/hunspell-1.6.2/intl/COPYING.LIB %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/66c77efd1cf9c70d4f982ea59487b2eeb6338e26
cp %{_builddir}/hunspell-1.6.2/license.hunspell %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/7e9367aa6f34c602c5175ef7a86ce800b05e339c
cp %{_builddir}/hunspell-1.6.2/license.myspell %{buildroot}/usr/share/package-licenses/compat-hunspell-soname1.6/a897c88546c86e1f1eaebd89bc101404d51e81cc
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/affixcompress
rm -f %{buildroot}/usr/bin/analyze
rm -f %{buildroot}/usr/bin/chmorph
rm -f %{buildroot}/usr/bin/hunspell
rm -f %{buildroot}/usr/bin/hunzip
rm -f %{buildroot}/usr/bin/hzip
rm -f %{buildroot}/usr/bin/ispellaff2myspell
rm -f %{buildroot}/usr/bin/makealias
rm -f %{buildroot}/usr/bin/munch
rm -f %{buildroot}/usr/bin/unmunch
rm -f %{buildroot}/usr/bin/wordforms
rm -f %{buildroot}/usr/bin/wordlist2hunspell
rm -f %{buildroot}/usr/include/hunspell/atypes.hxx
rm -f %{buildroot}/usr/include/hunspell/csutil.hxx
rm -f %{buildroot}/usr/include/hunspell/htypes.hxx
rm -f %{buildroot}/usr/include/hunspell/hunspell.h
rm -f %{buildroot}/usr/include/hunspell/hunspell.hxx
rm -f %{buildroot}/usr/include/hunspell/hunvisapi.h
rm -f %{buildroot}/usr/include/hunspell/w_char.hxx
rm -f %{buildroot}/usr/lib64/libhunspell-1.6.so
rm -f %{buildroot}/usr/lib64/pkgconfig/hunspell.pc
rm -f %{buildroot}/usr/share/man/hu/man1/hunspell.1
rm -f %{buildroot}/usr/share/man/man1/hunspell.1
rm -f %{buildroot}/usr/share/man/man1/hunzip.1
rm -f %{buildroot}/usr/share/man/man1/hzip.1
rm -f %{buildroot}/usr/share/man/man3/hunspell.3
rm -f %{buildroot}/usr/share/man/man5/hunspell.5

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhunspell-1.6.so.0
/usr/lib64/libhunspell-1.6.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-hunspell-soname1.6/66c77efd1cf9c70d4f982ea59487b2eeb6338e26
/usr/share/package-licenses/compat-hunspell-soname1.6/7e9367aa6f34c602c5175ef7a86ce800b05e339c
/usr/share/package-licenses/compat-hunspell-soname1.6/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/compat-hunspell-soname1.6/a897c88546c86e1f1eaebd89bc101404d51e81cc
/usr/share/package-licenses/compat-hunspell-soname1.6/aba8d76d0af67d57da3c3c321caa59f3d242386b
/usr/share/package-licenses/compat-hunspell-soname1.6/f45ee1c765646813b442ca58de72e20a64a7ddba
