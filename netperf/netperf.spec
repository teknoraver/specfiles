%global commit bcb868bde7f0203bbab69609f65d4088ba7398db
%global date 20180613
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:       Network Performance Testing Tool
Name:          netperf
Version:       2.7.1
Release:       0%{?commit:.%{date}git%{shortcommit}}%{?dist}

Group:         System Environment/Base
License:       Unknown
URL:           https://hewlettpackard.github.io/netperf/
Source:        https://github.com/HewlettPackard/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc, automake, texinfo, texinfo-tex

# we are not quite ready to make this a requirement but leave
# the line here as a heads up for the attentive :)
# BuildRequires: libsmbios-devel

# if you want to enable the SCTP tests, append --enable-sctp to the
# configure line, and uncomment the next line
BuildRequires: lksctp-tools-devel

%description
Many different network benchmarking tools are collected in this package,
maintained by Rick Jones of HP.


%prep
%setup -q -n %{name}-%{commit}

%build
# gcc 4.4 users may want to disable the strict aliasing warnings
# CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"
./autogen.sh
%configure --enable-unixdomain --enable-sctp --enable-dccp
make  %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}

# Convert the main netperf document to other formats
make -C doc %{name}.txt %{name}.html %{name}.xml pdf

# We don't want to package the Makefile files in the examples directory
rm -f doc/examples/Makefile*

# Info
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING Release_Notes
%doc doc/netperf.{html,pdf,txt,xml}
%doc doc/examples
%{_mandir}/man1/*
%{_infodir}/*
%{_bindir}/netperf
%{_bindir}/netserver


%changelog
* Mon Oct 28 2019 Timothy Redaelli <tredaelli@redhat.com> - 2.7.1-0.20180613gitbcb868b
- Use the correct versioning for a git release

* Tue Oct  2 2018 Matteo Croce <mcroce@redhat.com> - 2.7.1-3
- Fedora 29 upload

* Mon Dec 18 2017 Matteo Croce <mcroce@redhat.com> - 2.7.1-1
- Specfile update for new Github repo

* Mon Sep  7 2009 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.4.5-1
- Specfile cleanup.

* Sat Jun 17 2006 Martin A. Brown <martin@linux-ip.net> - 2.4.2-1
- initial contributed specfile for netperf package (v2.4.2)
