#include <stdio.h>
#include <iostream>
#include <assert.h>
#include "circom.hpp"
#include "calcwit.hpp"
void ToBits_0_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void ToBits_0_run(uint ctx_index,Circom_CalcWit* ctx);
void SHA2_224_256_padding_1_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void SHA2_224_256_padding_1_run(uint ctx_index,Circom_CalcWit* ctx);
void Sha224_initial_value_2_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Sha224_initial_value_2_run(uint ctx_index,Circom_CalcWit* ctx);
void XOR3_v2_3_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void XOR3_v2_3_run(uint ctx_index,Circom_CalcWit* ctx);
void Bits34_4_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Bits34_4_run(uint ctx_index,Circom_CalcWit* ctx);
void SHA2_224_256_schedule_5_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void SHA2_224_256_schedule_5_run(uint ctx_index,Circom_CalcWit* ctx);
void SHA2_224_256_round_keys_6_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void SHA2_224_256_round_keys_6_run(uint ctx_index,Circom_CalcWit* ctx);
void Bits2_7_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Bits2_7_run(uint ctx_index,Circom_CalcWit* ctx);
void Bits35_8_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Bits35_8_run(uint ctx_index,Circom_CalcWit* ctx);
void SHA2_224_256_compress_inner_9_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void SHA2_224_256_compress_inner_9_run(uint ctx_index,Circom_CalcWit* ctx);
void Bits33_10_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Bits33_10_run(uint ctx_index,Circom_CalcWit* ctx);
void SHA2_224_256_rounds_11_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void SHA2_224_256_rounds_11_run(uint ctx_index,Circom_CalcWit* ctx);
void Sha224_hash_bits_12_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Sha224_hash_bits_12_run(uint ctx_index,Circom_CalcWit* ctx);
void DWordsToByteString_13_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void DWordsToByteString_13_run(uint ctx_index,Circom_CalcWit* ctx);
void Sha224_hash_bits_digest_14_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Sha224_hash_bits_digest_14_run(uint ctx_index,Circom_CalcWit* ctx);
void Num2Bits_15_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Num2Bits_15_run(uint ctx_index,Circom_CalcWit* ctx);
void Bits2Num_16_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Bits2Num_16_run(uint ctx_index,Circom_CalcWit* ctx);
void Num2Bits_17_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Num2Bits_17_run(uint ctx_index,Circom_CalcWit* ctx);
void Main_18_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather);
void Main_18_run(uint ctx_index,Circom_CalcWit* ctx);
Circom_TemplateFunction _functionTable[19] = { 
ToBits_0_run,
SHA2_224_256_padding_1_run,
Sha224_initial_value_2_run,
XOR3_v2_3_run,
Bits34_4_run,
SHA2_224_256_schedule_5_run,
SHA2_224_256_round_keys_6_run,
Bits2_7_run,
Bits35_8_run,
SHA2_224_256_compress_inner_9_run,
Bits33_10_run,
SHA2_224_256_rounds_11_run,
Sha224_hash_bits_12_run,
DWordsToByteString_13_run,
Sha224_hash_bits_digest_14_run,
Num2Bits_15_run,
Bits2Num_16_run,
Num2Bits_17_run,
Main_18_run };
Circom_TemplateFunction _functionTableParallel[19] = { 
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL,
NULL };
uint get_main_input_signal_start() {return 2;}

uint get_main_input_signal_no() {return 3;}

uint get_total_signal_no() {return 96145;}

uint get_number_of_components() {return 9504;}

uint get_size_of_input_hashmap() {return 256;}

uint get_size_of_witness() {return 23950;}

uint get_size_of_constants() {return 145;}

uint get_size_of_io_map() {return 0;}

void release_memory_component(Circom_CalcWit* ctx, uint pos) {{

if (pos != 0){{

if(ctx->componentMemory[pos].subcomponents)
delete []ctx->componentMemory[pos].subcomponents;

if(ctx->componentMemory[pos].subcomponentsParallel)
delete []ctx->componentMemory[pos].subcomponentsParallel;

if(ctx->componentMemory[pos].outputIsSet)
delete []ctx->componentMemory[pos].outputIsSet;

if(ctx->componentMemory[pos].mutexes)
delete []ctx->componentMemory[pos].mutexes;

if(ctx->componentMemory[pos].cvs)
delete []ctx->componentMemory[pos].cvs;

if(ctx->componentMemory[pos].sbct)
delete []ctx->componentMemory[pos].sbct;

}}


}}


// function declarations
// template declarations
void ToBits_0_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 0;
ctx->componentMemory[coffset].templateName = "ToBits";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void ToBits_0_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[7];
FrElement lvar[3];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[0]); // line circom 57
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 64],&lvar[2]); // line circom 58
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 58
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 0)]); // line circom 59
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 0)],&expaux[3]); // line circom 59
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 59
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 59. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[2]); // line circom 60
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 0)]); // line circom 60
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 60
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 57
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[0]); // line circom 57
}
Fr_eq(&expaux[0],&signalValues[mySignalStart + 64],&lvar[1]); // line circom 63
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 63. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void SHA2_224_256_padding_1_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 1;
ctx->componentMemory[coffset].templateName = "SHA2_224_256_padding";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 253;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[1]{0};
}

void SHA2_224_256_padding_1_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[4];
FrElement lvar[5];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
{
uint aux_create = 0;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+765;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "len_tb";
ToBits_0_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 65 ;
aux_cmp_num += 1;
}
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[4]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[3]); // line circom 23
while(Fr_isTrue(&expaux[0])){
Fr_mod(&expaux[0],&lvar[3],&circuitConstants[4]); // line circom 24
{
PFrElement aux_dest = &signalValues[mySignalStart + ((0 + (1 * Fr_toInt(&expaux[0]))) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 512)]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 23
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[3]); // line circom 23
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 253];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[5]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[6]); // line circom 28
while(Fr_isTrue(&expaux[0])){
Fr_mod(&expaux[0],&lvar[3],&circuitConstants[4]); // line circom 28
{
PFrElement aux_dest = &signalValues[mySignalStart + ((0 + (1 * Fr_toInt(&expaux[0]))) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 28
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[6]); // line circom 28
}
{
uint cmp_index_ref = 0;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 64];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
ToBits_0_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 32
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_add(&expaux[0],&circuitConstants[6],&lvar[3]); // line circom 33
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_mod(&expaux[0],&lvar[4],&circuitConstants[4]); // line circom 34
{
PFrElement aux_dest = &signalValues[mySignalStart + ((0 + (1 * Fr_toInt(&expaux[0]))) + 0)];
// load src
Fr_sub(&expaux[1],&circuitConstants[7],&lvar[3]); // line circom 34
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[0]].signalStart + ((1 * Fr_toInt(&expaux[1])) + 0)]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 32
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 32
}
for (uint i = 0; i < 1; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Sha224_initial_value_2_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 2;
ctx->componentMemory[coffset].templateName = "Sha224_initial_value";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 0;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
Sha224_initial_value_2_run(coffset,ctx);
}

void Sha224_initial_value_2_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[4];
FrElement lvar[10];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[8]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[9]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[11]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[13]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[15]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[17]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[19]);
}
{
PFrElement aux_dest = &lvar[7];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[21]);
}
{
PFrElement aux_dest = &lvar[8];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[8],&circuitConstants[22]); // line circom 21
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[9];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[23]); // line circom 22
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[8])) + (1 * Fr_toInt(&lvar[9]))) + 0)];
// load src
Fr_shr(&expaux[1],&lvar[((1 * Fr_toInt(&lvar[8])) + 0)],&lvar[9]); // line circom 23
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 23
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[9];
// load src
Fr_add(&expaux[0],&lvar[9],&circuitConstants[2]); // line circom 22
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[23]); // line circom 22
}
{
PFrElement aux_dest = &lvar[8];
// load src
Fr_add(&expaux[0],&lvar[8],&circuitConstants[2]); // line circom 21
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[8],&circuitConstants[22]); // line circom 21
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void XOR3_v2_3_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 3;
ctx->componentMemory[coffset].templateName = "XOR3_v2";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 3;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void XOR3_v2_3_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[12];
FrElement lvar[0];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &signalValues[mySignalStart + 4];
// load src
Fr_mul(&expaux[0],&signalValues[mySignalStart + 2],&signalValues[mySignalStart + 3]); // line circom 45
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
Fr_mul(&expaux[9],&circuitConstants[10],&signalValues[mySignalStart + 2]); // line circom 46
Fr_sub(&expaux[7],&circuitConstants[2],&expaux[9]); // line circom 46
Fr_mul(&expaux[8],&circuitConstants[10],&signalValues[mySignalStart + 3]); // line circom 46
Fr_sub(&expaux[6],&expaux[7],&expaux[8]); // line circom 46
Fr_mul(&expaux[7],&circuitConstants[14],&signalValues[mySignalStart + 4]); // line circom 46
Fr_add(&expaux[5],&expaux[6],&expaux[7]); // line circom 46
Fr_mul(&expaux[3],&signalValues[mySignalStart + 1],&expaux[5]); // line circom 46
Fr_add(&expaux[2],&expaux[3],&signalValues[mySignalStart + 2]); // line circom 46
Fr_add(&expaux[1],&expaux[2],&signalValues[mySignalStart + 3]); // line circom 46
Fr_mul(&expaux[2],&circuitConstants[10],&signalValues[mySignalStart + 4]); // line circom 46
Fr_sub(&expaux[0],&expaux[1],&expaux[2]); // line circom 46
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Bits34_4_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 4;
ctx->componentMemory[coffset].templateName = "Bits34";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Bits34_4_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[8];
FrElement lvar[2];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 99
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&lvar[1]); // line circom 100
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 100
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 101
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)],&expaux[3]); // line circom 101
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 101
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 101. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[1]); // line circom 102
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 102
Fr_add(&expaux[0],&lvar[0],&expaux[2]); // line circom 102
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 99
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 99
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 34];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[23]); // line circom 105
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 105
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 35];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[24]); // line circom 106
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 106
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 34]); // line circom 107
Fr_mul(&expaux[1],&signalValues[mySignalStart + 34],&expaux[3]); // line circom 107
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 107
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 107. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 35]); // line circom 108
Fr_mul(&expaux[1],&signalValues[mySignalStart + 35],&expaux[3]); // line circom 108
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 108
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 108. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_mul(&expaux[5],&circuitConstants[25],&signalValues[mySignalStart + 34]); // line circom 110
Fr_add(&expaux[3],&lvar[0],&expaux[5]); // line circom 110
Fr_mul(&expaux[4],&circuitConstants[26],&signalValues[mySignalStart + 35]); // line circom 110
Fr_add(&expaux[2],&expaux[3],&expaux[4]); // line circom 110
Fr_eq(&expaux[0],&signalValues[mySignalStart + 33],&expaux[2]); // line circom 110
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 110. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &signalValues[mySignalStart + 32];
// load src
// end load src
Fr_copy(aux_dest,&lvar[0]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void SHA2_224_256_schedule_5_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 5;
ctx->componentMemory[coffset].templateName = "SHA2_224_256_schedule";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 512;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[3120]{0};
}

void SHA2_224_256_schedule_5_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[8];
FrElement lvar[7];
uint sub_component_aux;
uint index_multiple_eq;
{
uint aux_create = 0;
int aux_cmp_num = 48+ctx_index+1;
uint csoffset = mySignalStart+4352;
uint aux_dimensions[2] = {48,32};
for (uint i = 0; i < 1536; i++) {
std::string new_cmp_name = "s0xor"+ctx->generate_position_array(aux_dimensions, 2, i);
XOR3_v2_3_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 5 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 1536;
int aux_cmp_num = 1584+ctx_index+1;
uint csoffset = mySignalStart+12032;
uint aux_dimensions[2] = {48,32};
for (uint i = 0; i < 1536; i++) {
std::string new_cmp_name = "s1xor"+ctx->generate_position_array(aux_dimensions, 2, i);
XOR3_v2_3_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 5 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 3072;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+2624;
uint aux_dimensions[1] = {48};
for (uint i = 0; i < 48; i++) {
std::string new_cmp_name = "modulo"+ctx->generate_position_array(aux_dimensions, 1, i);
Bits34_4_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 36 ;
aux_cmp_num += 1;
}
}
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[27]); // line circom 17
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[23]); // line circom 19
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[2]); // line circom 19
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[0])) + (1 * Fr_toInt(&lvar[2]))) + 64)]); // line circom 19
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 19
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 19
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[23]); // line circom 19
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[0])) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&lvar[1]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[0])) + 576)];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[0])) + 64)],32);
}
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_add(&expaux[0],&lvar[0],&circuitConstants[2]); // line circom 17
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[27]); // line circom 17
}
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[27]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[0]); // line circom 28
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_sub(&expaux[0],&lvar[0],&circuitConstants[27]); // line circom 29
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_sub(&expaux[0],&lvar[0],&circuitConstants[28]); // line circom 30
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_sub(&expaux[0],&lvar[0],&circuitConstants[10]); // line circom 31
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[23]); // line circom 36
while(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 0);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 1];
// load src
Fr_add(&expaux[2],&lvar[6],&circuitConstants[20]); // line circom 42
Fr_mod(&expaux[1],&expaux[2],&circuitConstants[23]); // line circom 42
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[2])) + (1 * Fr_toInt(&expaux[1]))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 0);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 2];
// load src
Fr_add(&expaux[2],&lvar[6],&circuitConstants[29]); // line circom 43
Fr_mod(&expaux[1],&expaux[2],&circuitConstants[23]); // line circom 43
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[2])) + (1 * Fr_toInt(&expaux[1]))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[30]); // line circom 44
if(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 0);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[2])) + (1 * (Fr_toInt(&lvar[6]) + 3))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
}else{
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 0);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 45
Fr_mul(&expaux[2],&expaux[3],&ctx->signalValues[ctx->componentMemory[mySubcomponents[(((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 0)]].signalStart + 0]); // line circom 45
Fr_add(&expaux[0],&lvar[4],&expaux[2]); // line circom 45
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 1536);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 1];
// load src
Fr_add(&expaux[2],&lvar[6],&circuitConstants[31]); // line circom 48
Fr_mod(&expaux[1],&expaux[2],&circuitConstants[23]); // line circom 48
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&expaux[1]))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 1536);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 2];
// load src
Fr_add(&expaux[2],&lvar[6],&circuitConstants[32]); // line circom 49
Fr_mod(&expaux[1],&expaux[2],&circuitConstants[23]); // line circom 49
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&expaux[1]))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[33]); // line circom 50
if(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 1536);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[3])) + (1 * (Fr_toInt(&lvar[6]) + 10))) + 576)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
}else{
{
uint cmp_index_ref = (((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 1536);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
}
{
PFrElement aux_dest = &lvar[5];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 51
Fr_mul(&expaux[2],&expaux[3],&ctx->signalValues[ctx->componentMemory[mySubcomponents[(((32 * Fr_toInt(&lvar[1])) + (1 * Fr_toInt(&lvar[6]))) + 1536)]].signalStart + 0]); // line circom 51
Fr_add(&expaux[0],&lvar[5],&expaux[2]); // line circom 51
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
Fr_add(&expaux[0],&lvar[6],&circuitConstants[2]); // line circom 36
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[23]); // line circom 36
}
{
PFrElement aux_dest = &lvar[6];
// load src
Fr_sub(&expaux[4],&lvar[0],&circuitConstants[20]); // line circom 55
Fr_add(&expaux[2],&lvar[5],&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[4])) + 0)]); // line circom 55
Fr_add(&expaux[1],&expaux[2],&lvar[4]); // line circom 55
Fr_sub(&expaux[2],&lvar[0],&circuitConstants[27]); // line circom 55
Fr_add(&expaux[0],&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[2])) + 0)]); // line circom 55
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[1])) + 3072);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
// end load src
Fr_copy(aux_dest,&lvar[6]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits34_4_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[0])) + 576)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[1])) + 3072)]].signalStart + 0],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[0])) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[1])) + 3072)]].signalStart + 32]);
}
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_add(&expaux[0],&lvar[0],&circuitConstants[2]); // line circom 28
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[0]); // line circom 28
}
for (uint i = 0; i < 3120; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void SHA2_224_256_round_keys_6_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 6;
ctx->componentMemory[coffset].templateName = "SHA2_224_256_round_keys";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 0;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
SHA2_224_256_round_keys_6_run(coffset,ctx);
}

void SHA2_224_256_round_keys_6_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[3];
FrElement lvar[65];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[35]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[36]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[37]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[38]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[39]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[40]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[41]);
}
{
PFrElement aux_dest = &lvar[7];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[42]);
}
{
PFrElement aux_dest = &lvar[8];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[43]);
}
{
PFrElement aux_dest = &lvar[9];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[45]);
}
{
PFrElement aux_dest = &lvar[10];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[46]);
}
{
PFrElement aux_dest = &lvar[11];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[48]);
}
{
PFrElement aux_dest = &lvar[12];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[50]);
}
{
PFrElement aux_dest = &lvar[13];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[52]);
}
{
PFrElement aux_dest = &lvar[14];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[54]);
}
{
PFrElement aux_dest = &lvar[15];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[55]);
}
{
PFrElement aux_dest = &lvar[16];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[56]);
}
{
PFrElement aux_dest = &lvar[17];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[57]);
}
{
PFrElement aux_dest = &lvar[18];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[58]);
}
{
PFrElement aux_dest = &lvar[19];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[59]);
}
{
PFrElement aux_dest = &lvar[20];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[61]);
}
{
PFrElement aux_dest = &lvar[21];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[63]);
}
{
PFrElement aux_dest = &lvar[22];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[64]);
}
{
PFrElement aux_dest = &lvar[23];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[66]);
}
{
PFrElement aux_dest = &lvar[24];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[68]);
}
{
PFrElement aux_dest = &lvar[25];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[70]);
}
{
PFrElement aux_dest = &lvar[26];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[72]);
}
{
PFrElement aux_dest = &lvar[27];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[74]);
}
{
PFrElement aux_dest = &lvar[28];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[76]);
}
{
PFrElement aux_dest = &lvar[29];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[77]);
}
{
PFrElement aux_dest = &lvar[30];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[79]);
}
{
PFrElement aux_dest = &lvar[31];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[81]);
}
{
PFrElement aux_dest = &lvar[32];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[82]);
}
{
PFrElement aux_dest = &lvar[33];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[83]);
}
{
PFrElement aux_dest = &lvar[34];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[85]);
}
{
PFrElement aux_dest = &lvar[35];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[87]);
}
{
PFrElement aux_dest = &lvar[36];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[89]);
}
{
PFrElement aux_dest = &lvar[37];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[91]);
}
{
PFrElement aux_dest = &lvar[38];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[93]);
}
{
PFrElement aux_dest = &lvar[39];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[95]);
}
{
PFrElement aux_dest = &lvar[40];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[97]);
}
{
PFrElement aux_dest = &lvar[41];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[99]);
}
{
PFrElement aux_dest = &lvar[42];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[101]);
}
{
PFrElement aux_dest = &lvar[43];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[103]);
}
{
PFrElement aux_dest = &lvar[44];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[105]);
}
{
PFrElement aux_dest = &lvar[45];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[107]);
}
{
PFrElement aux_dest = &lvar[46];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[109]);
}
{
PFrElement aux_dest = &lvar[47];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[111]);
}
{
PFrElement aux_dest = &lvar[48];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[113]);
}
{
PFrElement aux_dest = &lvar[49];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[115]);
}
{
PFrElement aux_dest = &lvar[50];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[117]);
}
{
PFrElement aux_dest = &lvar[51];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[119]);
}
{
PFrElement aux_dest = &lvar[52];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[121]);
}
{
PFrElement aux_dest = &lvar[53];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[123]);
}
{
PFrElement aux_dest = &lvar[54];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[125]);
}
{
PFrElement aux_dest = &lvar[55];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[127]);
}
{
PFrElement aux_dest = &lvar[56];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[129]);
}
{
PFrElement aux_dest = &lvar[57];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[131]);
}
{
PFrElement aux_dest = &lvar[58];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[133]);
}
{
PFrElement aux_dest = &lvar[59];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[135]);
}
{
PFrElement aux_dest = &lvar[60];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[137]);
}
{
PFrElement aux_dest = &lvar[61];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[139]);
}
{
PFrElement aux_dest = &lvar[62];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[141]);
}
{
PFrElement aux_dest = &lvar[63];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[142]);
}
{
PFrElement aux_dest = &lvar[64];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[64],&circuitConstants[0]); // line circom 21
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[64])) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&lvar[((1 * Fr_toInt(&lvar[64])) + 0)]);
}
{
PFrElement aux_dest = &lvar[64];
// load src
Fr_add(&expaux[0],&lvar[64],&circuitConstants[2]); // line circom 21
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[64],&circuitConstants[0]); // line circom 21
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Bits2_7_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 7;
ctx->componentMemory[coffset].templateName = "Bits2";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Bits2_7_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[6];
FrElement lvar[0];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
Fr_band(&expaux[0],&signalValues[mySignalStart + 2],&circuitConstants[2]); // line circom 11
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 1];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 2],&circuitConstants[2]); // line circom 12
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 12
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 0]); // line circom 14
Fr_mul(&expaux[1],&signalValues[mySignalStart + 0],&expaux[3]); // line circom 14
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 14
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 14. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 1]); // line circom 15
Fr_mul(&expaux[1],&signalValues[mySignalStart + 1],&expaux[3]); // line circom 15
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 15
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 15. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_mul(&expaux[3],&circuitConstants[10],&signalValues[mySignalStart + 1]); // line circom 17
Fr_add(&expaux[2],&expaux[3],&signalValues[mySignalStart + 0]); // line circom 17
Fr_eq(&expaux[0],&signalValues[mySignalStart + 2],&expaux[2]); // line circom 17
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 17. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Bits35_8_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 8;
ctx->componentMemory[coffset].templateName = "Bits35";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Bits35_8_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[9];
FrElement lvar[2];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 124
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&lvar[1]); // line circom 125
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 125
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 126
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)],&expaux[3]); // line circom 126
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 126
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 126. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[1]); // line circom 127
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 127
Fr_add(&expaux[0],&lvar[0],&expaux[2]); // line circom 127
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 124
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 124
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 34];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[23]); // line circom 130
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 130
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 35];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[24]); // line circom 131
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 131
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 36];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[84]); // line circom 132
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 132
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 34]); // line circom 133
Fr_mul(&expaux[1],&signalValues[mySignalStart + 34],&expaux[3]); // line circom 133
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 133
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 133. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 35]); // line circom 134
Fr_mul(&expaux[1],&signalValues[mySignalStart + 35],&expaux[3]); // line circom 134
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 134
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 134. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 36]); // line circom 135
Fr_mul(&expaux[1],&signalValues[mySignalStart + 36],&expaux[3]); // line circom 135
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 135
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 135. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_mul(&expaux[6],&circuitConstants[25],&signalValues[mySignalStart + 34]); // line circom 137
Fr_add(&expaux[4],&lvar[0],&expaux[6]); // line circom 137
Fr_mul(&expaux[5],&circuitConstants[26],&signalValues[mySignalStart + 35]); // line circom 137
Fr_add(&expaux[3],&expaux[4],&expaux[5]); // line circom 137
Fr_mul(&expaux[4],&circuitConstants[143],&signalValues[mySignalStart + 36]); // line circom 137
Fr_add(&expaux[2],&expaux[3],&expaux[4]); // line circom 137
Fr_eq(&expaux[0],&signalValues[mySignalStart + 33],&expaux[2]); // line circom 137
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 137. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &signalValues[mySignalStart + 32];
// load src
// end load src
Fr_copy(aux_dest,&lvar[0]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void SHA2_224_256_compress_inner_9_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 9;
ctx->componentMemory[coffset].templateName = "SHA2_224_256_compress_inner";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 196;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[98]{0};
}

void SHA2_224_256_compress_inner_9_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[8];
FrElement lvar[7];
uint sub_component_aux;
uint index_multiple_eq;
{
uint aux_create = 0;
int aux_cmp_num = 2+ctx_index+1;
uint csoffset = mySignalStart+498;
uint aux_dimensions[1] = {32};
for (uint i = 0; i < 32; i++) {
std::string new_cmp_name = "major"+ctx->generate_position_array(aux_dimensions, 1, i);
Bits2_7_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 3 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 32;
int aux_cmp_num = 34+ctx_index+1;
uint csoffset = mySignalStart+594;
uint aux_dimensions[1] = {32};
for (uint i = 0; i < 32; i++) {
std::string new_cmp_name = "s0xor"+ctx->generate_position_array(aux_dimensions, 1, i);
XOR3_v2_3_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 5 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 64;
int aux_cmp_num = 66+ctx_index+1;
uint csoffset = mySignalStart+754;
uint aux_dimensions[1] = {32};
for (uint i = 0; i < 32; i++) {
std::string new_cmp_name = "s1xor"+ctx->generate_position_array(aux_dimensions, 1, i);
XOR3_v2_3_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 5 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 96;
int aux_cmp_num = 1+ctx_index+1;
uint csoffset = mySignalStart+461;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "decompose_e";
Bits35_8_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 37 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 97;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+424;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "decompose_a";
Bits35_8_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 37 ;
aux_cmp_num += 1;
}
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 161];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 325],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 129];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 293],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 64];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 228],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 32];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 196],32);
}
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[23]); // line circom 41
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[2]); // line circom 42
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 260)]); // line circom 42
Fr_add(&expaux[0],&lvar[0],&expaux[2]); // line circom 42
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[2]); // line circom 43
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[2])) + 357)]); // line circom 43
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 43
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 41
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[23]); // line circom 41
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 96];
// load src
// end load src
Fr_copy(aux_dest,&lvar[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 193];
// load src
// end load src
Fr_copy(aux_dest,&lvar[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[23]); // line circom 59
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 390)];
// load src
Fr_sub(&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 325)],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 357)]); // line circom 62
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 293)],&expaux[3]); // line circom 62
Fr_add(&expaux[0],&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 357)]); // line circom 62
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 63
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 390)]); // line circom 63
Fr_add(&expaux[0],&lvar[5],&expaux[2]); // line circom 63
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 0);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 2];
// load src
Fr_add(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 196)],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 228)]); // line circom 67
Fr_add(&expaux[0],&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[6])) + 260)]); // line circom 67
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits2_7_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 68
Fr_mul(&expaux[2],&expaux[3],&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[6])) + 0)]].signalStart + 1]); // line circom 68
Fr_add(&expaux[0],&lvar[4],&expaux[2]); // line circom 68
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 32);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 1];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[10]); // line circom 71
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 71
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 196)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 32);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 2];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[51]); // line circom 72
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 72
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 196)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 32);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[33]); // line circom 73
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 73
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 196)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 74
Fr_mul(&expaux[2],&expaux[3],&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[6])) + 32)]].signalStart + 0]); // line circom 74
Fr_add(&expaux[0],&lvar[2],&expaux[2]); // line circom 74
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 64);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 1];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[18]); // line circom 77
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 77
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 293)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 64);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 2];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[47]); // line circom 78
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 78
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 293)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[6])) + 64);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 3];
// load src
Fr_add(&expaux[1],&lvar[6],&circuitConstants[69]); // line circom 79
Fr_mod(&expaux[0],&expaux[1],&circuitConstants[23]); // line circom 79
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 293)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
XOR3_v2_3_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[6]); // line circom 80
Fr_mul(&expaux[2],&expaux[3],&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[6])) + 64)]].signalStart + 0]); // line circom 80
Fr_add(&expaux[0],&lvar[3],&expaux[2]); // line circom 80
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
Fr_add(&expaux[0],&lvar[6],&circuitConstants[2]); // line circom 59
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[6],&circuitConstants[23]); // line circom 59
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 422];
// load src
Fr_add(&expaux[4],&signalValues[mySignalStart + 292],&signalValues[mySignalStart + 389]); // line circom 84
Fr_add(&expaux[3],&expaux[4],&lvar[3]); // line circom 84
Fr_add(&expaux[2],&expaux[3],&lvar[5]); // line circom 84
Fr_add(&expaux[1],&expaux[2],&signalValues[mySignalStart + 195]); // line circom 84
Fr_add(&expaux[0],&expaux[1],&signalValues[mySignalStart + 194]); // line circom 84
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 423];
// load src
Fr_add(&expaux[5],&signalValues[mySignalStart + 389],&lvar[3]); // line circom 85
Fr_add(&expaux[4],&expaux[5],&lvar[5]); // line circom 85
Fr_add(&expaux[3],&expaux[4],&signalValues[mySignalStart + 195]); // line circom 85
Fr_add(&expaux[2],&expaux[3],&signalValues[mySignalStart + 194]); // line circom 85
Fr_add(&expaux[1],&expaux[2],&lvar[2]); // line circom 85
Fr_add(&expaux[0],&expaux[1],&lvar[4]); // line circom 85
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
uint cmp_index_ref = 96;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + 422]);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Bits35_8_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 97];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[96]].signalStart + 0],32);
}
{
uint cmp_index_ref = 97;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + 423]);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Bits35_8_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[97]].signalStart + 0],32);
}
for (uint i = 0; i < 98; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Bits33_10_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 10;
ctx->componentMemory[coffset].templateName = "Bits33";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Bits33_10_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[7];
FrElement lvar[2];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 76
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&lvar[1]); // line circom 77
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 77
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 78
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)],&expaux[3]); // line circom 78
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 78
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 78. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[1]); // line circom 79
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[1])) + 0)]); // line circom 79
Fr_add(&expaux[0],&lvar[0],&expaux[2]); // line circom 79
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 76
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[23]); // line circom 76
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 34];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 33],&circuitConstants[23]); // line circom 82
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 82
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&circuitConstants[2],&signalValues[mySignalStart + 34]); // line circom 83
Fr_mul(&expaux[1],&signalValues[mySignalStart + 34],&expaux[3]); // line circom 83
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 83
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 83. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
Fr_mul(&expaux[4],&circuitConstants[25],&signalValues[mySignalStart + 34]); // line circom 85
Fr_add(&expaux[2],&lvar[0],&expaux[4]); // line circom 85
Fr_eq(&expaux[0],&signalValues[mySignalStart + 33],&expaux[2]); // line circom 85
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 85. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &signalValues[mySignalStart + 32];
// load src
// end load src
Fr_copy(aux_dest,&lvar[0]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void SHA2_224_256_rounds_11_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 11;
ctx->componentMemory[coffset].templateName = "SHA2_224_256_rounds";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 320;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[73]{0};
}

void SHA2_224_256_rounds_11_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[7];
FrElement lvar[10];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[0]);
}
{
uint aux_create = 0;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+13258;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "RC";
SHA2_224_256_round_keys_6_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 64 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 1;
int aux_cmp_num = 1+ctx_index+1;
uint csoffset = mySignalStart+13322;
uint aux_dimensions[1] = {64};
for (uint i = 0; i < 64; i++) {
std::string new_cmp_name = "compress"+ctx->generate_position_array(aux_dimensions, 1, i);
SHA2_224_256_compress_inner_9_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 914 ;
aux_cmp_num += 99;
}
}
{
uint aux_create = 65;
int aux_cmp_num = 6337+ctx_index+1;
uint csoffset = mySignalStart+71818;
uint aux_dimensions[1] = {8};
for (uint i = 0; i < 8; i++) {
std::string new_cmp_name = "modulo"+ctx->generate_position_array(aux_dimensions, 1, i);
Bits33_10_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 35 ;
aux_cmp_num += 1;
}
}
if (!Fr_isTrue(&circuitConstants[2])) std::cout << "Failed assert in template/function " << myTemplateName << " line 13. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&circuitConstants[2]));
if (!Fr_isTrue(&circuitConstants[2])) std::cout << "Failed assert in template/function " << myTemplateName << " line 14. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&circuitConstants[2]));
{
PFrElement aux_dest = &signalValues[mySignalStart + 13186];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[0]].signalStart + 0],64);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 576];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 320],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 2656];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 352],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 4736];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 384],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 6881];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 448],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 8961];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 480],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 11041];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 512],32);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[23]); // line circom 43
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_shl(&expaux[4],&circuitConstants[2],&lvar[3]); // line circom 44
Fr_mul(&expaux[2],&signalValues[mySignalStart + ((96 + (1 * Fr_toInt(&lvar[3]))) + 320)],&expaux[4]); // line circom 44
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 44
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_shl(&expaux[4],&circuitConstants[2],&lvar[3]); // line circom 45
Fr_mul(&expaux[2],&signalValues[mySignalStart + ((224 + (1 * Fr_toInt(&lvar[3]))) + 320)],&expaux[4]); // line circom 45
Fr_add(&expaux[0],&lvar[2],&expaux[2]); // line circom 45
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 43
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[23]); // line circom 43
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 6816];
// load src
// end load src
Fr_copy(aux_dest,&lvar[1]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 13121];
// load src
// end load src
Fr_copy(aux_dest,&lvar[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 51
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[5],&circuitConstants[23]); // line circom 53
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[5]); // line circom 54
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&lvar[5]))) + 320)]); // line circom 54
Fr_add(&expaux[0],&lvar[4],&expaux[2]); // line circom 54
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
Fr_add(&expaux[0],&lvar[5],&circuitConstants[2]); // line circom 53
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[5],&circuitConstants[23]); // line circom 53
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 13250)];
// load src
// end load src
Fr_copy(aux_dest,&lvar[4]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 51
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 51
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 61
while(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 194];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 256)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 195];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 13186)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 196];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 576)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 228];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 2656)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 260];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 4736)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 292];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 6816)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 293];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 6881)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 325];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 8961)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 357];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[3])) + 11041)],32);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 32)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[3])) + 1);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 389];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 13121)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
SHA2_224_256_compress_inner_9_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 576)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 0],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 2656)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 32],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 4736)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 64],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * (Fr_toInt(&lvar[3]) + 1)) + 6816)];
// load src
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 96]);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 6881)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 97],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 8961)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 129],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * (Fr_toInt(&lvar[3]) + 1)) + 11041)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 161],32);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * (Fr_toInt(&lvar[3]) + 1)) + 13121)];
// load src
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[3])) + 1)]].signalStart + 193]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 61
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[0]); // line circom 61
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 88
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 88
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 88
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[7];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[8];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[9];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[23]); // line circom 98
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 99
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 576)]); // line circom 99
Fr_add(&expaux[0],&lvar[3],&expaux[2]); // line circom 99
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 100
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 2656)]); // line circom 100
Fr_add(&expaux[0],&lvar[4],&expaux[2]); // line circom 100
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[5];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 101
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 4736)]); // line circom 101
Fr_add(&expaux[0],&lvar[5],&expaux[2]); // line circom 101
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[6];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 102
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 6881)]); // line circom 102
Fr_add(&expaux[0],&lvar[6],&expaux[2]); // line circom 102
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[7];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 103
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 8961)]); // line circom 103
Fr_add(&expaux[0],&lvar[7],&expaux[2]); // line circom 103
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[8];
// load src
Fr_shl(&expaux[3],&circuitConstants[2],&lvar[9]); // line circom 104
Fr_mul(&expaux[2],&expaux[3],&signalValues[mySignalStart + ((2048 + (1 * Fr_toInt(&lvar[9]))) + 11041)]); // line circom 104
Fr_add(&expaux[0],&lvar[8],&expaux[2]); // line circom 104
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[9];
// load src
Fr_add(&expaux[0],&lvar[9],&circuitConstants[2]); // line circom 98
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[23]); // line circom 98
}
{
uint cmp_index_ref = 65;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13250],&lvar[3]); // line circom 107
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 66;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13251],&lvar[4]); // line circom 108
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 67;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13252],&lvar[5]); // line circom 109
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 68;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13253],&signalValues[mySignalStart + 6880]); // line circom 110
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 69;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13254],&lvar[6]); // line circom 111
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 70;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13255],&lvar[7]); // line circom 112
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 71;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13256],&lvar[8]); // line circom 113
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 72;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 33];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 13257],&signalValues[mySignalStart + 13185]); // line circom 114
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Bits33_10_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[9];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[22]); // line circom 116
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[9])) + 0)];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[9])) + 65)]].signalStart + 0],32);
}
{
PFrElement aux_dest = &lvar[9];
// load src
Fr_add(&expaux[0],&lvar[9],&circuitConstants[2]); // line circom 116
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[9],&circuitConstants[22]); // line circom 116
}
for (uint i = 0; i < 73; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Sha224_hash_bits_12_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 12;
ctx->componentMemory[coffset].templateName = "Sha224_hash_bits";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 253;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[4]{0};
}

void Sha224_hash_bits_12_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[5];
FrElement lvar[5];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
{
uint aux_create = 0;
int aux_cmp_num = 1+ctx_index+1;
uint csoffset = mySignalStart+1757;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "pad";
SHA2_224_256_padding_1_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 830 ;
aux_cmp_num += 2;
}
}
{
uint aux_create = 1;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+1501;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "iv";
Sha224_initial_value_2_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 256 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 2;
int aux_cmp_num = 6349+ctx_index+1;
uint csoffset = mySignalStart+74685;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "sch";
SHA2_224_256_schedule_5_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 19712 ;
aux_cmp_num += 3121;
}
}
{
uint aux_create = 3;
int aux_cmp_num = 3+ctx_index+1;
uint csoffset = mySignalStart+2587;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "rds";
SHA2_224_256_rounds_11_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 72098 ;
aux_cmp_num += 6346;
}
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
uint cmp_index_ref = 0;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 512];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 224],253);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 253;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
SHA2_224_256_padding_1_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 477];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[0]].signalStart + 0],512);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 989];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[1]].signalStart + 0],256);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 34
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[27]); // line circom 39
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[4],&circuitConstants[23]); // line circom 40
while(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = 2;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + (((32 * Fr_toInt(&lvar[3])) + (1 * Fr_toInt(&lvar[4]))) + 64)];
// load src
Fr_mul(&expaux[1],&lvar[3],&circuitConstants[23]); // line circom 41
Fr_sub(&expaux[2],&circuitConstants[80],&lvar[4]); // line circom 41
Fr_add(&expaux[0],&expaux[1],&expaux[2]); // line circom 41
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + ((0 + (1 * Fr_toInt(&expaux[0]))) + 477)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
SHA2_224_256_schedule_5_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_add(&expaux[0],&lvar[4],&circuitConstants[2]); // line circom 40
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[4],&circuitConstants[23]); // line circom 40
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 39
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[27]); // line circom 39
}
{
uint cmp_index_ref = 3;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 256];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[2]].signalStart + 0],64);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 64)){
SHA2_224_256_rounds_11_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
uint cmp_index_ref = 3;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 320];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 989],256);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 256)){
SHA2_224_256_rounds_11_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 1245];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[3]].signalStart + 0],256);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 34
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[20]); // line circom 51
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((32 * Fr_toInt(&lvar[2])) + 0)];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + ((256 + (32 * Fr_toInt(&lvar[2]))) + 989)],32);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 51
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[20]); // line circom 51
}
for (uint i = 0; i < 4; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void DWordsToByteString_13_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 13;
ctx->componentMemory[coffset].templateName = "DWordsToByteString";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 224;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void DWordsToByteString_13_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[7];
FrElement lvar[5];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[20]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[20]); // line circom 226
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[14]); // line circom 227
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[4],&circuitConstants[22]); // line circom 230
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_shl(&expaux[4],&circuitConstants[2],&lvar[4]); // line circom 231
Fr_mul(&expaux[2],&signalValues[mySignalStart + (((32 * Fr_toInt(&lvar[1])) + (1 * ((Fr_toInt(&lvar[2]) * 8) + Fr_toInt(&lvar[4])))) + 28)],&expaux[4]); // line circom 231
Fr_add(&expaux[0],&lvar[3],&expaux[2]); // line circom 231
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[4];
// load src
Fr_add(&expaux[0],&lvar[4],&circuitConstants[2]); // line circom 230
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[4],&circuitConstants[22]); // line circom 230
}
Fr_mul(&expaux[1],&lvar[1],&circuitConstants[14]); // line circom 234
Fr_sub(&expaux[2],&circuitConstants[12],&lvar[2]); // line circom 234
Fr_add(&expaux[0],&expaux[1],&expaux[2]); // line circom 234
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&expaux[0])) + 0)];
// load src
// end load src
Fr_copy(aux_dest,&lvar[3]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&circuitConstants[2]); // line circom 227
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[2],&circuitConstants[14]); // line circom 227
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 226
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[20]); // line circom 226
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Sha224_hash_bits_digest_14_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 14;
ctx->componentMemory[coffset].templateName = "Sha224_hash_bits_digest";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 253;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[2]{0};
}

void Sha224_hash_bits_digest_14_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[2];
FrElement lvar[1];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
{
uint aux_create = 0;
int aux_cmp_num = 1+ctx_index+1;
uint csoffset = mySignalStart+533;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "sha";
Sha224_hash_bits_12_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 94397 ;
aux_cmp_num += 9471;
}
}
{
uint aux_create = 1;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+281;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "ser";
DWordsToByteString_13_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 252 ;
aux_cmp_num += 1;
}
}
{
uint cmp_index_ref = 0;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 224];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 28],253);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 253;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Sha224_hash_bits_12_run(mySubcomponents[cmp_index_ref],ctx);
}
{
uint cmp_index_ref = 1;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 28];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[0]].signalStart + 0],224);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 224;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
DWordsToByteString_13_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[1]].signalStart + 0],28);
}
for (uint i = 0; i < 2; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Num2Bits_15_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 15;
ctx->componentMemory[coffset].templateName = "Num2Bits";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Num2Bits_15_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[6];
FrElement lvar[4];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[3]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[3]); // line circom 31
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 253],&lvar[3]); // line circom 32
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 32
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&circuitConstants[2]); // line circom 33
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&expaux[3]); // line circom 33
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 33
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 33. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_mul(&expaux[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&lvar[2]); // line circom 34
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 34
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&lvar[2]); // line circom 35
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 31
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[3]); // line circom 31
}
Fr_eq(&expaux[0],&lvar[1],&signalValues[mySignalStart + 253]); // line circom 38
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 38. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Bits2Num_16_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 16;
ctx->componentMemory[coffset].templateName = "Bits2Num";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 224;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Bits2Num_16_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[5];
FrElement lvar[4];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[144]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[144]); // line circom 61
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_mul(&expaux[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 1)],&lvar[2]); // line circom 62
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 62
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&lvar[2]); // line circom 63
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 61
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[144]); // line circom 61
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
// end load src
Fr_copy(aux_dest,&lvar[1]);
}
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Num2Bits_17_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 17;
ctx->componentMemory[coffset].templateName = "Num2Bits";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 1;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[0];
}

void Num2Bits_17_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[6];
FrElement lvar[4];
uint sub_component_aux;
uint index_multiple_eq;
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[22]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[2]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 31
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)];
// load src
Fr_shr(&expaux[1],&signalValues[mySignalStart + 8],&lvar[3]); // line circom 32
Fr_band(&expaux[0],&expaux[1],&circuitConstants[2]); // line circom 32
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_sub(&expaux[3],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&circuitConstants[2]); // line circom 33
Fr_mul(&expaux[1],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&expaux[3]); // line circom 33
Fr_eq(&expaux[0],&expaux[1],&circuitConstants[1]); // line circom 33
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 33. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_mul(&expaux[2],&signalValues[mySignalStart + ((1 * Fr_toInt(&lvar[3])) + 0)],&lvar[2]); // line circom 34
Fr_add(&expaux[0],&lvar[1],&expaux[2]); // line circom 34
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[2];
// load src
Fr_add(&expaux[0],&lvar[2],&lvar[2]); // line circom 35
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
PFrElement aux_dest = &lvar[3];
// load src
Fr_add(&expaux[0],&lvar[3],&circuitConstants[2]); // line circom 31
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[3],&circuitConstants[22]); // line circom 31
}
Fr_eq(&expaux[0],&lvar[1],&signalValues[mySignalStart + 8]); // line circom 38
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 38. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
for (uint i = 0; i < 0; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void Main_18_create(uint soffset,uint coffset,Circom_CalcWit* ctx,std::string componentName,uint componentFather){
ctx->componentMemory[coffset].templateId = 18;
ctx->componentMemory[coffset].templateName = "Main";
ctx->componentMemory[coffset].signalStart = soffset;
ctx->componentMemory[coffset].inputCounter = 3;
ctx->componentMemory[coffset].componentName = componentName;
ctx->componentMemory[coffset].idFather = componentFather;
ctx->componentMemory[coffset].subcomponents = new uint[31]{0};
}

void Main_18_run(uint ctx_index,Circom_CalcWit* ctx){
FrElement* signalValues = ctx->signalValues;
u64 mySignalStart = ctx->componentMemory[ctx_index].signalStart;
std::string myTemplateName = ctx->componentMemory[ctx_index].templateName;
std::string myComponentName = ctx->componentMemory[ctx_index].componentName;
u64 myFather = ctx->componentMemory[ctx_index].idFather;
u64 myId = ctx_index;
u32* mySubcomponents = ctx->componentMemory[ctx_index].subcomponents;
bool* mySubcomponentsParallel = ctx->componentMemory[ctx_index].subcomponentsParallel;
FrElement* circuitConstants = ctx->circuitConstants;
std::string* listOfTemplateMessages = ctx->listOfTemplateMessages;
FrElement expaux[5];
FrElement lvar[2];
uint sub_component_aux;
uint index_multiple_eq;
{
uint aux_create = 0;
int aux_cmp_num = 30+ctx_index+1;
uint csoffset = mySignalStart+1214;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "sha224";
Sha224_hash_bits_digest_14_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 94930 ;
aux_cmp_num += 9473;
}
}
{
uint aux_create = 1;
int aux_cmp_num = 29+ctx_index+1;
uint csoffset = mySignalStart+960;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "num2bits";
Num2Bits_15_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 254 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 2;
int aux_cmp_num = 0+ctx_index+1;
uint csoffset = mySignalStart+483;
for (uint i = 0; i < 1; i++) {
std::string new_cmp_name = "bits2num";
Bits2Num_16_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 225 ;
aux_cmp_num += 1;
}
}
{
uint aux_create = 3;
int aux_cmp_num = 1+ctx_index+1;
uint csoffset = mySignalStart+708;
uint aux_dimensions[1] = {28};
for (uint i = 0; i < 28; i++) {
std::string new_cmp_name = "byteToBits"+ctx->generate_position_array(aux_dimensions, 1, i);
Num2Bits_17_create(csoffset,aux_cmp_num,ctx,new_cmp_name,myId);
mySubcomponents[aux_create+i] = aux_cmp_num;
csoffset += 9 ;
aux_cmp_num += 1;
}
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 4];
// load src
Fr_add(&expaux[0],&signalValues[mySignalStart + 2],&signalValues[mySignalStart + 3]); // line circom 21
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
{
printf("cr_id_t_id");
}
{
printf(" ");
}
{
char* temp = Fr_element2str(&signalValues[mySignalStart + 4]);
printf("%s",temp);
delete [] temp;
}
{
printf("\n");
}
{
uint cmp_index_ref = 1;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 253];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + 4]);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Num2Bits_15_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 5];
// load src
// end load src
Fr_copyn(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[1]].signalStart + 0],253);
}
{
uint cmp_index_ref = 0;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 28];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 5],253);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 253;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Sha224_hash_bits_digest_14_run(mySubcomponents[cmp_index_ref],ctx);
}
{
printf("c_id");
}
{
printf(" ");
}
{
char* temp = Fr_element2str(&signalValues[mySignalStart + 1]);
printf("%s",temp);
delete [] temp;
}
{
printf("\n");
}
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[75]); // line circom 31
while(Fr_isTrue(&expaux[0])){
{
uint cmp_index_ref = ((1 * Fr_toInt(&lvar[0])) + 3);
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 8];
// load src
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[0]].signalStart + ((1 * Fr_toInt(&lvar[0])) + 0)]);
}
// run sub component if needed
if(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 1)){
Num2Bits_17_run(mySubcomponents[cmp_index_ref],ctx);

}
}
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_add(&expaux[0],&lvar[0],&circuitConstants[2]); // line circom 31
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[75]); // line circom 31
}
{
PFrElement aux_dest = &lvar[0];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[75]); // line circom 35
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &lvar[1];
// load src
// end load src
Fr_copy(aux_dest,&circuitConstants[1]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[22]); // line circom 36
while(Fr_isTrue(&expaux[0])){
{
PFrElement aux_dest = &signalValues[mySignalStart + ((1 * ((Fr_toInt(&lvar[0]) * 8) + Fr_toInt(&lvar[1]))) + 258)];
// load src
Fr_sub(&expaux[2],&circuitConstants[20],&lvar[1]); // line circom 37
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[((1 * Fr_toInt(&lvar[0])) + 3)]].signalStart + ((1 * Fr_toInt(&expaux[2])) + 0)]);
}
{
PFrElement aux_dest = &lvar[1];
// load src
Fr_add(&expaux[0],&lvar[1],&circuitConstants[2]); // line circom 36
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[1],&circuitConstants[22]); // line circom 36
}
{
PFrElement aux_dest = &lvar[0];
// load src
Fr_add(&expaux[0],&lvar[0],&circuitConstants[2]); // line circom 35
// end load src
Fr_copy(aux_dest,&expaux[0]);
}
Fr_lt(&expaux[0],&lvar[0],&circuitConstants[75]); // line circom 35
}
{
uint cmp_index_ref = 2;
{
PFrElement aux_dest = &ctx->signalValues[ctx->componentMemory[mySubcomponents[cmp_index_ref]].signalStart + 1];
// load src
// end load src
Fr_copyn(aux_dest,&signalValues[mySignalStart + 258],224);
}
// need to run sub component
ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter -= 224;
assert(!(ctx->componentMemory[mySubcomponents[cmp_index_ref]].inputCounter));
Bits2Num_16_run(mySubcomponents[cmp_index_ref],ctx);
}
{
PFrElement aux_dest = &signalValues[mySignalStart + 482];
// load src
// end load src
Fr_copy(aux_dest,&ctx->signalValues[ctx->componentMemory[mySubcomponents[2]].signalStart + 0]);
}
{
printf("c_id_out");
}
{
printf(" ");
}
{
char* temp = Fr_element2str(&signalValues[mySignalStart + 482]);
printf("%s",temp);
delete [] temp;
}
{
printf("\n");
}
Fr_eq(&expaux[0],&signalValues[mySignalStart + 1],&signalValues[mySignalStart + 482]); // line circom 43
if (!Fr_isTrue(&expaux[0])) std::cout << "Failed assert in template/function " << myTemplateName << " line 43. " <<  "Followed trace of components: " << ctx->getTrace(myId) << std::endl;
assert(Fr_isTrue(&expaux[0]));
{
PFrElement aux_dest = &signalValues[mySignalStart + 0];
// load src
// end load src
Fr_copy(aux_dest,&signalValues[mySignalStart + 482]);
}
for (uint i = 0; i < 31; i++){
uint index_subc = ctx->componentMemory[ctx_index].subcomponents[i];
if (index_subc != 0)release_memory_component(ctx,index_subc);
}
}

void run(Circom_CalcWit* ctx){
Main_18_create(1,0,ctx,"main",0);
Main_18_run(0,ctx);
}

