#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Socket-Socks
Version  : 0.74
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/O/OL/OLEG/IO-Socket-Socks-0.74.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OL/OLEG/IO-Socket-Socks-0.74.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-socks-perl/libio-socket-socks-perl_0.74-1.debian.tar.xz
Summary  : 'Provides a way to create socks client or server both 4 and 5 version.'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-IO-Socket-Socks-license = %{version}-%{release}
Requires: perl-IO-Socket-Socks-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This module seeks to provide a full implementation of the SOCKS protocol
while behaving like a regular socket as much as possible.

%package dev
Summary: dev components for the perl-IO-Socket-Socks package.
Group: Development
Provides: perl-IO-Socket-Socks-devel = %{version}-%{release}
Requires: perl-IO-Socket-Socks = %{version}-%{release}

%description dev
dev components for the perl-IO-Socket-Socks package.


%package license
Summary: license components for the perl-IO-Socket-Socks package.
Group: Default

%description license
license components for the perl-IO-Socket-Socks package.


%package perl
Summary: perl components for the perl-IO-Socket-Socks package.
Group: Default
Requires: perl-IO-Socket-Socks = %{version}-%{release}

%description perl
perl components for the perl-IO-Socket-Socks package.


%prep
%setup -q -n IO-Socket-Socks-0.74
cd %{_builddir}
tar xf %{_sourcedir}/libio-socket-socks-perl_0.74-1.debian.tar.xz
cd %{_builddir}/IO-Socket-Socks-0.74
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Socket-Socks-0.74/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Socks
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Socket-Socks/80ffcbf4dda8583a3a2797d95daf3cf575f62376
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Socket::Socks.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Socket-Socks/80ffcbf4dda8583a3a2797d95daf3cf575f62376

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
