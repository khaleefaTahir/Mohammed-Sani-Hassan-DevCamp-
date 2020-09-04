create database devcamp;
use devcamp;
create table Building (BuildingID int, complexID int, BuildingName varchar(100), Address varchar(100));
create table Apartments (AptID int, UnitNumber varchar(10), BuildingID int);
create table Requests (RequestID int, Status varchar(100), AptID int, Description varchar(100));
create table Complexes (ComplexID int, ComplexName varchar(100));
create table Tenants (TenantID int, TenantsName varchar(100));
create table AptTenants (TenantID int, AptID int);