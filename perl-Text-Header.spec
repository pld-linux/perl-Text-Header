#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Header
Summary:	Text::Header - RFC 822/2068 `header' and `unheader' functions
Summary(pl):	Text::Header - funkcje header i unheader dla RFC 822/2068
Name:		perl-Text-Header
Version:	1.03
Release:	1
# licenses given explicitly, not "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2dce923006b849ae20a54a8afd31f8af
URL:		http://search.cpan.org/dist/Text-Header/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides two new functions, `header' and `unheader', which
provide general-purpose RFC 822 header construction and parsing. They
do not provide any intelligent defaults of HTTP-specific methods. They
are simply aimed at providing an easy means to address the mechanics
of header parsing.

%description -l pl
Ten modu³ dostarcza dwie nowe funkcje: header i unheader,
udostêpniaj±ce konstruowanie i przetwarzanie nag³ówków zgodnych z RFC
822 do zastosowañ ogólnych. Nie dostarczaj± ¿adnych inteligentnych
warto¶ci domy¶lnych dla metod specyficznych dla HTTP. Maj± na celu po
prostu dostarczenie ³atwego mechanizmu do przetwarzania nag³ówków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Header.pm
%{_mandir}/man3/*
