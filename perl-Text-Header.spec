#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Header
Summary:	-
Name:		perl-Text-Header
Version:	1.03
Release:	0
# note if it is "same as perl"
#   This module is free software; you may copy this under the terms of the
#   GNU General Public License, or the Artistic License, copies of which
#   should have accompanied your Perl kit.
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2dce923006b849ae20a54a8afd31f8af
#URL:		-
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
This module provides two new functions, `header' and `unheader', which
provide general-purpose RFC 822 header construction and parsing. They do
not provide any intelligent defaults of HTTP-specific methods. They are
simply aimed at providing an easy means to address the mechanics of
header parsing.

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
