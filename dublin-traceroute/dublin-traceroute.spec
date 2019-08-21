Name: dublin-traceroute
Version: 0.4.2
Release: 3
Summary: Dublin Traceroute is a NAT-aware multipath tracerouting tool
License: BSD
BuildRequires: gcc-c++, cmake, libtins-devel, libtins, jsoncpp-devel, libpcap-devel
Source: https://github.com/insomniacslk/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/teknoraver/specfiles/master/%{name}.patch
Patch0: %{name}.patch
Requires: libcap

%description
Dublin Traceroute is a NAT-aware multipath traceroute tool.

Dublin Traceroute uses the techniques invented by the authors of
Paris-traceroute to enumerate the paths of ECMP flow-based load balancing,
but introduces a new technique for NAT detection.

%prep
%setup -q
%patch0 -p1

%build
echo $RPM_BUILD_ROOT
%cmake .
%make_build

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%doc COPYING documentation/readme/
%{_bindir}/dublin-traceroute
%exclude /usr/lib/debug/
%exclude %{_includedir}/

%post
setcap CAP_NET_RAW+ep %{_bindir}/dublin-traceroute
