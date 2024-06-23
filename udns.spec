Summary:	udns library tools
Summary(pl.UTF-8):	Narzędzia korzystające z biblioteki udns
Name:		udns
Version:	0.5
Release:	1
License:	LGPL v2.1+
Group:		Networking/Utilities
Source0:	http://www.corpit.ru/mjt/udns/%{name}-%{version}.tar.gz
# Source0-md5:	c8508d27dc82a812bd41153107e9ae7e
URL:		http://www.corpit.ru/mjt/udns.html
Requires:	%{name}-libs = %{version}-%{release}
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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -W" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version},%{_includedir},%{_libdir},%{_mandir}/man{1,3}}

install dnsget_s $RPM_BUILD_ROOT%{_bindir}/dnsget
install ex-rdns_s $RPM_BUILD_ROOT%{_bindir}/ex-rdns
install rblcheck_s $RPM_BUILD_ROOT%{_bindir}/rblcheck
install libudns.* $RPM_BUILD_ROOT%{_libdir}
cp -fd libudns_s.so $RPM_BUILD_ROOT%{_libdir}/libudns.so
cp -p ex-rdns.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p udns.h $RPM_BUILD_ROOT%{_includedir}
cp -p *.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p *.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dnsget
%attr(755,root,root) %{_bindir}/rblcheck
%{_mandir}/man1/dnsget.1*
%{_mandir}/man1/rblcheck.1*

%files libs
%defattr(644,root,root,755)
%doc NEWS NOTES TODO
%attr(755,root,root) %{_libdir}/libudns.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex-rdns
%attr(755,root,root) %{_libdir}/libudns.so
%{_includedir}/udns.h
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/udns.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libudns.a
