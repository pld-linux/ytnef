# NOTE: for versions >= 1:1.9 (after merge with libytnef) see libytnef.spec
%include	/usr/lib/rpm/macros.perl
Summary:	Yerase's TNEF Stream Reader
Summary(pl.UTF-8):	Czytnik strumieni TNET autorstwa Yerase
Name:		ytnef
Version:	2.6
Release:	3.1
License:	GPL v2+
Group:		Libraries
# note: development continued on https://github.com/Yeraze/ytnef
Source0:	http://downloads.sourceforge.net/ytnef/%{name}-%{version}.tar.gz
# Source0-md5:	572830ff0664a2abc3e7aea79040c338
Patch0:		%{name}-snprintf.patch
Patch1:		%{name}-filenames.patch
Patch2:		%{name}-snprintf2.patch
Patch3:		fix-ytnefprocess.patch
URL:		https://github.com/Yeraze/ytnef
BuildRequires:	libytnef-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yerase's TNEF Stream Reader. Can take a TNEF Stream (winmail.dat)
sent from Microsoft Outlook (or similar products) and extract the
attachments, including construction of Contact Cards & Calendar
entries.

%description -l pl.UTF-8
Czytnik strumieni TNET autorstwa Yerase - potrafi przyjąć strumień
TNEF (winmail.dat) wysłany w programu Microsoft Outlook (lub
podobnego) i wydobyć załączniki, w tym tworzenie kart kontaktowych
oraz wpisów kalendarza.

%prep
%setup -q
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/ytnef
%attr(755,root,root) %{_bindir}/ytnefprint
%attr(755,root,root) %{_bindir}/ytnefprocess.pl
