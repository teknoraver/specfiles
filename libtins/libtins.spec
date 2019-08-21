Name: libtins
Version: 4.2
Release: 4
Summary: High-level, multiplatform C++ network packet sniffing and crafting library
License: BSD
BuildRequires: gcc-c++, cmake, libpcap-devel, boost-devel
Source: https://github.com/mfontanini/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

%description
libtins is a high-level, multiplatform C++ network packet sniffing
and crafting library.

Its main purpose is to provide the C++ developer an easy, efficient,
platform and endianess-independent way to create tools which need to send,
receive and manipulate specially crafted packets.

%package devel
Requires: libtins
Summary: libtins development package

%description devel
This package provides libtins headers for developers.

%prep
%setup -q

%build
# C++11 support was added in GCC 4.8.1:
# https://www.gnu.org/software/gcc/projects/cxx-status.html#cxx11
ver=$(g++ -E -dM -o - - </dev/null |awk '/__GNUC__/{ver=$3}/__GNUC_MINOR__/{min=$3}/__GNUC_PATCHLEVEL__/{pl=$3}END{print ver*10000+min*100+pl}')
[ $ver -ge 40801 ] && cxx11=-DLIBTINS_ENABLE_CXX11=1 || :
%cmake . $cxx11 -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%make_build

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%doc {README,CONTRIBUTING,CHANGES}.md
%{_libdir}/libtins.so
%{_libdir}/libtins.so.%{version}

%files devel
%doc examples/
%{_includedir}/tins/
%{_libdir}/pkgconfig/libtins.pc
%exclude /usr/lib/cmake/
