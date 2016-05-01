Summary:	udns library tools
Summary(pl.UTF-8):	Narzędzia korzystające z biblioteki udns
Name:		udns
Version:	0.0.9
Release:	2
License:	LGPL
Group:		Networking/Utilities
Source0:	http://www.corpit.ru/mjt/udns/%{name}_%{version}.tar.gz
# Source0-md5:	78843added6f6b690bc6019ab8ef03c9
URL:		http://www.corpit.ru/mjt/udns.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnsget and rblcheck tools using udns library.

%description -l pl.UTF-8
dnsget i rblcheck używające biblioteki udns.

%package libs
Summary:	A library that performs asynchronous DNS operations
Summary(pl.UTF-8):	Biblioteka do wykonywania asynchronicznych zapytań DNS
Group:		Libraries

%description libs
A library that performs asynchronous DNS operations.

%description libs -l pl.UTF-8
Biblioteka do wykonywania asynchronicznych zapytań DNS.

%package devel
Summary:	Header files for udns library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki udns
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for udns library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki udns.

%package static
Summary:	Static udns library
Summary(pl.UTF-8):	Statyczna biblioteka udns
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static udns library.

%description static -l pl.UTF-8
Statyczna biblioteka udns.

%prep
%setup -q

%build
./configure
%{__make} staticlib sharedlib dnsget_s ex-rdns_s rblcheck_s \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version},%{_includedir},%{_libdir},%{_mandir}/man{1,3}}

install dnsget_s $RPM_BUILD_ROOT%{_bindir}/dnsget
install ex-rdns_s $RPM_BUILD_ROOT%{_bindir}/ex-rdns
install ex-rdns.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install rblcheck_s $RPM_BUILD_ROOT%{_bindir}/rblcheck
install udns.h $RPM_BUILD_ROOT%{_includedir}
install libudns.* $RPM_BUILD_ROOT%{_libdir}
cp -fd libudns_s.so $RPM_BUILD_ROOT%{_libdir}/libudns.so
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dnsget
%attr(755,root,root) %{_bindir}/rblcheck
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc NEWS NOTES TODO
%attr(755,root,root) %{_bindir}/ex-rdns
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
